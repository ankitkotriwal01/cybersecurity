import nmap
import json


class NmapCipherDetector:
    def detect_ciphers(self, host) -> None:
        """
        Detect the ciphers configured in the target system.

        Args:
            host (str): The target host to scan.
        """
        nm = nmap.PortScanner()

        # Run the script to detect SSL/TLS ciphers on port 443 (HTTPS)
        scan_results = nm.scan(hosts=host, arguments="--script ssl-enum-ciphers -p 443")

        # Print the results in a pretty-printed JSON format
        print(json.dumps(scan_results, indent=4))


if __name__ == "__main__":
    cipher_detector = NmapCipherDetector()
    # Replace 'example.com' with the target host
    cipher_detector.detect_ciphers('thehappyfinance.com')  # Example: 'example.com'
