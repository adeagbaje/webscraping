import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/news'

url_htmltext_request = requests.get(url).text

soup_object = BeautifulSoup(url_htmltext_request, 'html.parser')

titlelink = soup_object.select('.titlelink')
subtext = soup_object.select('.subtext')

def my_news(links, subtext):
    my_news = []
    for index, item in enumerate(links):
        title = titlelink[index].getText()
        href = titlelink[index].get('href', None)
        point = subtext[index].select('.score')
        if len(point) > 0:
            point = point[0].getText()
            my_news.append({'title': title, 'href': href, 'votes': point})
        
    return my_news

print(my_news(titlelink, subtext))
