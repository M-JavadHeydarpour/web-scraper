from core import Scrape
from spider import Spider


def main():
    sc = Scrape()
    sp = Spider()
    for url in sp.urls:
        response = sp.htmlDownloader(url)
        soup = sc.processHTML(response)
        yield sc.storeHTMLIntoJson(soup, url)


def core():
    url = 'resources/test.html'
    soup = Scrape.processHTML(url)
    return Scrape.storeHTMLIntoJson(soup)


if __name__ == "__main__":
    core()      # test html to json converter
    # main()    # when spider developing completed using this code
