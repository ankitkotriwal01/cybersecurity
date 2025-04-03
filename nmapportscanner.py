import nmap
import json

class NmapPortScanner:
    def port_scan(self, host, ports="1-1024") -> None:
        """
        Scan open ports on the target host.

        Args:
            host (string): IP address or hostname to scan
            ports (string): The range of ports to scan (default is "1-1024")
        """
        # Initialize the PortScanner object
        nm = nmap.PortScanner()

        try:
            # Run a port scan on the given host and port range
            print(f"Scanning {host} for open ports in range {ports}...")
            scan_results = nm.scan(hosts=host, arguments=f"-p {ports}")

            # Check if the host is up
            if nm.all_hosts():
                # Display scan results in a pretty JSON format
                print(json.dumps(scan_results, indent=4))
            else:
                print(f"No hosts found for {host}")

        except nmap.nmap.PortScannerError as e:
            print(f"Error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")


if __name__ == "__main__":
    host = '76.223.105.230'  # Replace with the target IP or hostname
    ports = '1-1024'  # Replace with port range (e.g., '1-1000', '80', '22-443')

    # Create an instance of NmapPortScanner and run the scan
    nmap_scanner = NmapPortScanner()
    nmap_scanner.port_scan(host, ports)
