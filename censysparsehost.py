import json
from censys.search import CensysHosts

censys_host = CensysHosts()

class CensysHostDetailsParser:
    def print_host_details(self, ip_address) -> None:
        try:
            ipinfo = censys_host.view(ip_address)
        except Exception as e:
            print(f"Error retrieving data for {ip_address}: {e}")
            return

        # Check if the 'services' key exists in the response and if it's not empty
        services = ipinfo.get('services', [])
        if services:
            # Safely access the first service's attributes
            first_service = services[0]
            service_name = first_service.get('service_name', 'N/A')
            port = first_service.get('port', 'N/A')
            banner = first_service.get('banner', 'N/A')

            # Print the details
            print('[services][0][service_name]: ', service_name)
            print('[services][0][port]: ', port)
            print('[services][0][banner]: ', banner)
        else:
            print("No services found for this IP address.")

if __name__ == "__main__":
    censys_host_details_parser = CensysHostDetailsParser()
    censys_host_details_parser.print_host_details('142.250.182.142')
