import requests
import json


class CrtshCrtInfo:
    def cert_query(self, host):
        """
        Perform a crt.sh certificates lookup for the host.

        Args:
            host (str): Host (domain or IP address)
        """
        try:
            # Define the URL for crt.sh search
            url = f"https://crt.sh/?q={host}&output=json"

            # Send a GET request to the crt.sh API
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                certs = response.json()

                # Check if any certificates were found
                if not certs:
                    print(f"No certificates found for {host}")
                else:
                    # Print the results as a formatted JSON
                    print(json.dumps(certs, indent=4, default=str))
            else:
                print(f"Error: Unable to fetch data from crt.sh (Status Code: {response.status_code})")

        except Exception as e:
            print(f"Error while querying crt.sh: {e}")


if __name__ == "__main__":
    cert_info = CrtshCrtInfo()
    cert_info.cert_query('76.223.105.230')  # Replace with the desired host
