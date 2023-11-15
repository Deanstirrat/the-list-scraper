# the-list-scraper
Uses foopee.com and spotify api to find all upcoming shows with artists you have saved songs by. Requires a Spotify developer account

# How to use:
1. Create a spotify developer account and create a new project
<img width="574" alt="Screenshot 2023-11-15 at 1 27 40 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/669160f0-32ba-40af-9f6e-c72eebaba431">
2. In the app settings, set redirect uri = http://localhost:1234
<img width="283" alt="Screenshot 2023-11-15 at 1 29 54 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/fb7862ba-07bf-429d-a278-c5f3d45a211e">
3. Get your client ID and secret
<img width="423" alt="Screenshot 2023-11-15 at 1 30 47 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/db04a22d-8625-4af4-840a-5d812482b9b6">
4. Paste them into the project
<img width="537" alt="Screenshot 2023-11-15 at 1 33 25 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/b1760a09-9058-484b-aee3-cb2b6c77e588">
5. Make sure neccesarry packages are installed
```
pip install beautifulsoup4 requests spotipy
```
6. Run the project
```
python theListScraper.py
```
