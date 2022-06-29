import requests
from bs4 import BeautifulSoup

url = 'https://bluelimelearning.github.io/my-fav-quotes/'

url_request = requests.get(url)

soup_object = BeautifulSoup(url_request.text, 'html.parser')

quotes = soup_object.findAll('div', {'class': 'quotes'})

for contents in quotes:
    fav_quote = contents.find('p', {'class': 'aquote'})
    quote = fav_quote.text.strip()

    fav_author = contents.find('p', {'class': 'author'})
    author = fav_author.text.strip()

    print(quote, '- ', author)

