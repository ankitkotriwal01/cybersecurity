""""needs an api key from google"""

import requests
class GoogleSearch:
    def __init__(self, api_key, cse_id):
        self.api_key = api_key
        self.cse_id = cse_id

    def perform_google_search(self, host, query_string):
        """
        Perform Google search using the host and query string using Google Custom Search API.

        Args:
            host (string): Target system
            query_string (string): Query string
        """
        query = f"site:{host} {query_string}"
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={self.api_key}&cx={self.cse_id}"
        try:
            response = requests.get(url)
            results = response.json()
            if 'items' in results:
                for item in results['items']:
                    print(item['link'])
            else:
                print("No results found.")
        except Exception as e:
            print(f"An error occurred during the search: {e}")

if __name__ == "__main__":
    api_key = 'YOUR_GOOGLE_API_KEY'
    cse_id = 'YOUR_CUSTOM_SEARCH_ENGINE_ID'

    google_search = GoogleSearch(api_key, cse_id)
    google_search.perform_google_search("example.com", 'inurl:"/wp-json/" -wordpress')
