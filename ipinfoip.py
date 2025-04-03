import json
import ipinfo

class IpinfoDetails:

    def __init__(self):
        # Use the default handler which does not require an API token
        self.handler = ipinfo.getHandler()

    def get_host_details(self, ip_address):
        try:
            # Fetch details for the given IP address
            ipinfo_details = self.handler.getDetails(ip_address)

            # Check if the details are returned and print them
            if ipinfo_details.all:
                print(json.dumps(ipinfo_details.all, indent=4))
            else:
                print("No details found for this IP address.")
        except Exception as e:
            # Catch any exceptions and print a user-friendly message
            print(f"An error occurred while fetching IP details: {e}")

if __name__ == "__main__":
    ipinfo_details = IpinfoDetails()

    # Replace with the actual IP address you want to query
    ipinfo_details.get_host_details('76.223.105.230')
