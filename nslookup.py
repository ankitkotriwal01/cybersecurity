import socket


class NetworkUtilites:
    def nslookup(self, domain):
        """
        Find the IP Address for a domain using socket.

        Args:
            domain (string): Domain that you want to find IP Address for
        """
        nslookup_result_ip = socket.gethostbyname(domain)
        print(nslookup_result_ip)


def test() -> None:
    network_utilities = NetworkUtilites()
    network_utilities.nslookup("google.com")
    network_utilities.nslookup("thehappyfinance.com")

test()