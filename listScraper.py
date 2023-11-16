import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tkinter import *
from tkinter import ttk

def listScraper(client_id, client_secret):
    # FOOPEE SCRAPER:
    band_names = {}

    urls = [
        "http://www.foopee.com/punk/the-list/by-band.0.html",
        "http://www.foopee.com/punk/the-list/by-band.1.html",
        "http://www.foopee.com/punk/the-list/by-band.2.html",
        "http://www.foopee.com/punk/the-list/by-band.3.html"
    ]

    print('finding shows');

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        band_li_tags = soup.select('li > a[name]')

        for tag in band_li_tags:
            band_name = tag.find('b').text.lower()
            shows = []
            for show_li in tag.find_next_sibling('ul').find_all('li'):
                date = show_li.find('a').text
                venue = show_li.find_all('a')[1].text
                shows.append((date, venue))
            if band_name in band_names:
                band_names[band_name].extend(shows)
            else:
                band_names[band_name] = shows


    # SPOTIFY API
    def find_artists(results):
        artist_names = {}
        for item in results['items']:
            for artist in item['track']['artists']:
                if artist['name'].lower() in band_names:
                    artist_name = artist['name'].lower()
                    if artist_name in artist_names:
                        artist_names[artist_name] += 1
                    else:
                        artist_names[artist_name] = 1
        return artist_names

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                redirect_uri="http://localhost:1234",
                                                scope="user-library-read"))

    results = sp.current_user_saved_tracks(limit=50)

    print('comparing to spotify library')
    artist_names = find_artists(results)
    numChecked = 49
    while results['next']:
        # print("searched: ", numChecked, " tracks")
        numChecked+=49
        results = sp.next(results)
        new_artists = find_artists(results)
        for new_artist, num_songs in new_artists.items():
            if new_artist in artist_names:
                artist_names[new_artist] += num_songs
            else:
                artist_names[new_artist] = 1

    results = []
    for artist, num_songs in sorted(artist_names.items(), key=lambda x: x[1], reverse=True):
        for show in band_names[artist]:
            date, venue = show
            results.append((artist, date, venue))
    return results

def findShows(*args):
    toggle_progress_bar()
    clientId = clientId_entry.get()
    clientSecret = clientSecret_entry.get()
    results = listScraper(clientId, clientSecret)
    for artist, date, venue in results:
        results_listbox.insert(END, f"Artist: {artist}, Show Date: {date}, Venue: {venue}")
    toggle_progress_bar()

def toggle_progress_bar():
    if progress_bar['value'] == 0:
        progress_bar.start()
    else:
        progress_bar.stop()

root = Tk()
root.title("Foopee Show Finder")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

clientId = StringVar()
clientId_entry = ttk.Entry(mainframe, width=25, textvariable=clientId)
clientId_entry.grid(column=2, row=1, sticky=(W, E))

clientSecret = StringVar()
clientSecret_entry = ttk.Entry(mainframe, width=25, textvariable=clientSecret)
clientSecret_entry.grid(column=2, row=2, sticky=(W, E))

progress_bar = ttk.Progressbar(mainframe, mode='indeterminate')
progress_bar.grid(column=2, row=5, sticky=(W, E))

ttk.Button(mainframe, text="Find Shows", command=findShows).grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Client ID").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Client Secret").grid(column=1, row=2, sticky=E)

results_listbox = Listbox(mainframe, width=50, height=10)
results_listbox.grid(column=2, row=4, sticky=(W, E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
progress_bar.grid(column=2, row=5, sticky=(W, E))

clientId_entry.focus()
root.bind("<Return>", findShows)

root.mainloop()