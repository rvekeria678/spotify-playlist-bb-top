from config.scrape import LIMIT
from config.url import BB_URL
from bs4 import BeautifulSoup
import requests

class BB_Scraper:
    def __init__(self, date) -> None:
        response = requests.get(f'{BB_URL}/{date}/')
        response.raise_for_status()
        bb_webpage = response.text

        soup = BeautifulSoup(bb_webpage, 'html.parser')

        cards = soup.find_all(name='div', class_='o-chart-results-list-row-container')

        titles = [el.find('ul').select('li ul li h3')[0].getText()
                  .replace('\t','').replace('\n','') for el in cards]
        artists = [el.find('ul').select('li ul li span')[0].getText()
                   .replace('\t','').replace('\n','') for el in cards]
        
        self.data = dict(zip(titles, artists))