

import json
from censys.search import CensysHosts

censys_host = CensysHosts()

class CensysHostDetails:
    def print_host_details(self, ip_address) -> dict:
        try:
            ipinfo = censys_host.view(ip_address)
        except Exception as e:
            print(f"Error retrieving data for {ip_address}: {e}")
            ipinfo = {}

        return ipinfo

if __name__ == "__main__":
    censys_info = CensysHostDetails()
    ip_address = '142.250.182.142'
    host_details = censys_info.print_host_details(ip_address)

    # Printing the JSON formatted data
    print(json.dumps(host_details, indent=4))
