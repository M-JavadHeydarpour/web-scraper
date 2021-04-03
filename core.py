#!/usr/bin/python3

from bs4 import BeautifulSoup
from io import BytesIO
import pycurl
from resources import config
import detectlanguage


class Scrape:
    def __init__(self):
        pass

    def processHTML(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        return soup

    def storeHTMLIntoJson(self, soup, url):

        title = soup.find('title').string
        date = soup.find('amp-timeago')['datetime']
        subtitle = ' '.join(soup.find('div', {"class": "sc-psorm hxxXzh"}).find('h1').string.split())
        author = soup.find('div', {'class': 'sc-psorm hxxXzh'}).find('a').string
        allParagraphs = self.getAllParagraph(soup)
        language = self.detectLanguage(allParagraphs[0])

        json_set = {'url': url, 'language': language, 'title': title, 'subtitle': subtitle, 'date': date,
                    'author': author, 'paragraphs': allParagraphs}

        return json_set

    def detectLanguage(self, data):
        detectlanguage.configuration.api_key = config.DETECT_LANGUAGE_API_KEY
        return detectlanguage.simple_detect(data)

    def getAllParagraph(self, soup):
        paragraphs = soup.find('div', {'class': 'article-premium'}).findAll('p')
        allParagraphs = []
        for paragraph in paragraphs:
            allParagraphs.append(' '.join(paragraph.text.split()))
        return allParagraphs

