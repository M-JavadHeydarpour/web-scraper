from resources import config
import requests


# TODO
class Spider:
    def __int__(self):
        self.urls = self.readUrls()

    def readUrls(self):
        with open(config.URLS, 'r') as file:
            for url in file:
                self.urls.append(url.rstrip('\n'))
        file.close()
        return self.urls

    def connection(self):
        pass

    def htmlDownloader(self, url):
        pass
