
from bs4 import BeautifulSoup
import requests


class WebScraping:
    def print_beautified_website_content(self, url) -> None:
        request = requests.get(url)

        soup = BeautifulSoup(request.content, 'html5lib')
        print(soup.prettify())


if __name__ == "__main__":
    web_scraping_content = WebScraping()
    web_scraping_content.print_beautified_website_content(
        'https://www.thehappyfinance.com')
