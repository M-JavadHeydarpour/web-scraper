#!/usr/bin/python3

from bs4 import BeautifulSoup
import pycurl
import config


class Scrape:
    def __init__(self):
        self.urls = []
        self.connection = []

    def readLinks(self):
        with open(config.URLS, 'r') as file:
            for url in file:
                self.urls.append(url.rstrip('\n'))
        file.close()

    def curlConnection(self):
        self.readLinks()
        for _ in self.urls:
            self.connection.append(pycurl.Curl())

    def getHTML(self):
        pass

    def storeHTML(self):
        pass

    def processHTML(self):
        pass

