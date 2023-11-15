import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# FOOPEE SCRAPER:
band_names = set()

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
    band_name_tags = soup.select('li > a[name] > b')
    new_band_names = set([tag.text.lower() for tag in band_name_tags])

    band_names.update(new_band_names)


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

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="815a2d977fb84893bda3ca19634084e3",
                                               client_secret="aabc70d3ef6e4f7eacff20f317251bcf",
                                               redirect_uri="http://localhost:1234",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks(limit=50)

print('comparing to spotify library')
artist_names = find_artists(results)
numChecked = 49
while results['next']:
    print("searched: ", numChecked, " tracks")
    numChecked+=19
    results = sp.next(results)
    new_artists = find_artists(results)
    for new_artist, num_songs in new_artists.items():
        if new_artist in artist_names:
            artist_names[new_artist] += num_songs
        else:
            artist_names[new_artist] = 1

for artist, num_songs in sorted(artist_names.items(), key=lambda x: x[1], reverse=True):
    print(artist)