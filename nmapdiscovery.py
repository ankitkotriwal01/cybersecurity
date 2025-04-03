import nmap
import json

class NmapDiscovery:
    def discover(self, host) -> None:
        """
        Discover hosts on the network using ARP.

        Args:
            host (string): IP or network to scan
        """
        # Create an Nmap object
        nm = nmap.PortScanner()

        # Run an ARP discovery scan with -PR (ARP) and -sn (ping scan)
        # For ARP scan, we use -PR, and -sn disables port scanning
        scan_results = nm.scan(hosts=host, arguments="-PR -sn")

        # Print the scan results in a pretty JSON format
        print(json.dumps(scan_results, indent=4))


if __name__ == "__main__":
    host = '76.223.105.230'  # Replace with your target IP range or single host
    nmap_discovery = NmapDiscovery()
    nmap_discovery.discover(host)
