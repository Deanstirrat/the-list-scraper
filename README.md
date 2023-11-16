# the-list-scraper
Uses foopee.com and spotify api to find bands/artists in your library that have performances in the Bay Area. Requires a Spotify developer account.

# How to use:
## 1. Create a spotify developer account and create a new project:
<img width="574" alt="Screenshot 2023-11-15 at 1 27 40 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/669160f0-32ba-40af-9f6e-c72eebaba431">


## 2. In the app settings, set redirect uri to "http://localhost:1234":
<img width="417" alt="Screenshot 2023-11-15 at 5 18 42 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/84d673f2-fb00-4c43-be2f-8ae284ab80d9">



## 3. Get your client ID and secret. You will paste these into the application:
<img width="423" alt="Screenshot 2023-11-15 at 1 30 47 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/db04a22d-8625-4af4-840a-5d812482b9b6">


## 4. Run the program
### 4.a. find folder where file is saved (on my desktop in this example):
<img width="309" alt="Screenshot 2023-11-15 at 5 22 08 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/48ee743a-715c-40c4-9b97-dcdd74f08bf8">

### 4.b. Open terminal and navigate to folder path with cd command (example: Desktop/the-list-scraper):
```
cd path/to/folder
```
<img width="510" alt="Screenshot 2023-11-15 at 5 23 48 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/d55fe5c4-faea-4ac4-bc26-1083c679277a">

### 4.c Install required libraries (run command in terminal):
```
pip install beautifulsoup4 requests spotipy
```

### 4.d. Run program with (run command in terminal)
```
python listScraper.py
```

## 5. Paste Client ID and Client Secret into the window
<img width="567" alt="Screenshot 2023-11-15 at 5 18 12 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/0d8f7292-1d84-40c7-8d1b-6b350c5cc48d">

## 6. Click find shows and wait for the shows to appear (may take longer based on number of saved songs)
<img width="542" alt="Screenshot 2023-11-15 at 5 17 46 PM" src="https://github.com/Deanstirrat/the-list-scraper/assets/37011725/c3428b1b-c5a0-4033-899c-e6b0b70d2706">



