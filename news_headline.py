from win32com.client import Dispatch
import requests
import pprint
import os
import sys
import re
#----------------------------------------

# function to retrieve the headlines from the Hindu


def hindu_news():
    '''retrieve the top headlines'''

    API_KEY = os.environ['news_api_key']

    payload = {
        "source": "the-hindu",
        "language": "en",
        "country": "in",
        "category": "general",
        "apiKey": API_KEY
    }

    try:
        resp = requests.get('https://newsapi.org/v2/top-headlines', params=payload)
    except:
        print('[ERROR]'.center(50, '-'))
        sys.exit()

    article = resp.json()

    results = []

    for ar in article['articles']:
        results.append(ar['title'])

    return results
#---------------------------------------------


news = hindu_news()

headlines = []
for i in range(len(news)):
    print(i + 1, news[i])
    headlines.append(re.findall('([\\w\\W \\S]+)\\s-', news[i]))


def read_news():
    speak = Dispatch('SAPI.Spvoice')
    speak.Speak(headlines)


with open('./today_headline.txt', 'w') as file:
    file.write('HEADLINE'.center(100))
    file.write('\n\n')

    for index, headline in enumerate(headlines, start=1):
        file.write(f'{index}.{headline[0]}')
        file.write('\n\n')

if __name__ == '__main__':
    hindu_news()
