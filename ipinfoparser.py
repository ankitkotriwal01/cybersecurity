import json
import ipinfo

class IpinfoDetails:

    def __init__(self):
        # Use the default handler (no access token required for free usage)
        self.handler = ipinfo.getHandler()

    def get_host_details(self, ip_address):
        try:
            # Fetch details for the given IP address
            ipinfo_details = self.handler.getDetails(ip_address)

            # Convert the response to JSON using json.dumps and then load it in a JSON object
            json_data = json.loads(json.dumps(ipinfo_details.all, indent=4))

            # Print the attributes we need
            print('City: ', json_data.get('city', 'Not Available'))
            print('Country: ', json_data.get('country', 'Not Available'))
            print('Timezone: ', json_data.get('timezone', 'Not Available'))
            print('Org: ', json_data.get('org', 'Not Available'))  # Added 'Org' (organization)

        except Exception as e:
            # Handle errors, e.g., invalid IP address or network issue
            print(f"An error occurred: {e}")
            print("Could not fetch details for the provided IP address.")

if __name__ == "__main__":
    ipinfo_details = IpinfoDetails()

    # Replace with the actual IP address you want to query
    ipinfo_details.get_host_details('142.250.182.46')  