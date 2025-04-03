import dns.resolver
import json


class DigInfo:
    def print_dig_info(self, host, record_type):
        """
        Get DNS information for the provided host.

        Args:
            host (str): The domain to query for.
            record_type (str): The type of DNS record (e.g., 'A', 'NS', 'CNAME').
        """
        try:
            # Perform the DNS query using dnspython
            answers = dns.resolver.resolve(host, record_type)

            # If records are found, print them
            print(f"{record_type} records for {host}:")
            for answer in answers:
                print(answer.to_text())

        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            print(f"No {record_type} records found for {host}.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    dig_info = DigInfo()

    # Print A and NS (DNS servers) records
    dig_info.print_dig_info('google.com', 'A')
    dig_info.print_dig_info('google.com', 'NS')
