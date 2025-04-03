from nslookup import Nslookup

class NsLookup:
    def nslookup(self, domain):
        """
        Perform a DNS lookup for a host.

        Args:
            domain (string): Domain that you want to find the IP Address for
        """

        try:
            # Use Google's public DNS server (8.8.8.8)
            dns_query = Nslookup(dns_servers=["8.8.8.8"])
            dns_record = dns_query.dns_lookup(domain)

            # Check if there were any answers in the DNS lookup
            if dns_record.answer:
                print(f"DNS Lookup for {domain}:")
                print(f"IP Addresses: {', '.join(dns_record.answer)}")
            else:
                print(f"No DNS records found for {domain}")

        except Exception as e:
            # Catch exceptions and print a message
            print(f"An error occurred while performing the DNS lookup: {e}")

if __name__ == "__main__":
    ns_lookup = NsLookup()
    ns_lookup.nslookup("google.com")  # Replace with any domain you want to query
