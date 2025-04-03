from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin  # To handle relative URLs


class WebCrawler:
    def print_beautified_website_content(self, url: str) -> None:
        try:
            # Use a requests session to handle the connection efficiently
            session = requests.Session()
            request = session.get(url)

            # Check if the request was successful (status code 200)
            if request.status_code == 200:
                # Parse the website content with BeautifulSoup
                soup = BeautifulSoup(request.content, 'html5lib')

                # Find all <a> tags and print the href attribute (links)
                print(f"Links from {url}:\n")
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href:
                        # Convert relative URL to absolute URL if necessary
                        absolute_url = urljoin(url, href)
                        print(absolute_url)
            else:
                print(f"Failed to retrieve content from {url}. Status code: {request.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while requesting the URL: {e}")


if __name__ == "__main__":
    web_crawler = WebCrawler()
    web_crawler.print_beautified_website_content('https://www.google.com')
    web_crawler.print_beautified_website_content('https://www.thehappyfinance.com')
