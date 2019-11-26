import urllib.parse
import urllib.request
from Singleton import SingletonType

class URLFetcher(metaclass=SingletonType):

    def __init__(self):
        self.urls = []

    def fetch(self,url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)
                self.urls.append(url)
    
    def dump_url_registry(self):
        return ', '.join(self.urls)


def main():
    MY_URLS = ['http://python.org',
                'http://google.com',
    ]


    fetcher = URLFetcher()
    for url in MY_URLS:
        try:
            fetcher.fetch(url)
        except Exception as e:
            print(e)
        
    print('---------------------------------------------------------------------')
    print('---------------------------------------------------------------------')
    done_urls = fetcher.dump_url_registry()
    print(f'Done URLS {done_urls}')
        
if __name__ == "__main__":
    main()
