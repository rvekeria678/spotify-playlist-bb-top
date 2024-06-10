from spotify_manager import SpotifyManager
from bb_scraper import BB_Scraper
from dotenv import load_dotenv
import os
import re
import datetime

#-----Date Logic-----#
def get_date() -> str:
    while True:
        date_input = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD:")
        if re.match(r'\d{4}-\d{2}-\d{2}', date_input): return date_input
        else: print("Invalid format. Please enter a date in the format 'YYYY-MM-DD' .")
def valid_date(date_str: str) -> bool:
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    current_date = datetime.datetime.now().date()
    return date_obj.date() < current_date
#-----Validation Logic -----#
date = get_date()
while not valid_date(date):
    print("Please enter a past date!")
    date = get_date()
#-----Creating Playlist-----#
#spotify_manager = SpotifyManager(playlist_data=(date,BB_Scraper(date=date).data))
spotify_manager = SpotifyManager()
spotify_manager.create_playlist(playlist_data=(date, BB_Scraper(date=date).data))