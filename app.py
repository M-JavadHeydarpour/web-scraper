from core import Scrape

if __name__ == "__main__":
    sc = Scrape()
    sc.curlConnection()
    print(sc.connection)
    print(sc.urls)
