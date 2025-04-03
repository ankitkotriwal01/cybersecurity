import psutil

class NetStats:
    def print_net_connections(self) -> None:
        try:
            print("TCP Connections:")
            tcp_connections = psutil.net_connections(kind='tcp')
            self._print_connections(tcp_connections)

            print("\nUDP Connections:")
            udp_connections = psutil.net_connections(kind='udp')
            self._print_connections(udp_connections)

        except Exception as e:
            print(f"An error occurred while fetching network connections: {e}")

    def _print_connections(self, connections) -> None:
        """
        Helper function to print connection details.
        """
        if not connections:
            print("No active connections found.")
            return

        for conn in connections:
            # Extract relevant details: local address, remote address, and connection status
            local_address = f"{conn.laddr.ip}:{conn.laddr.port}"
            remote_address = f"{conn.raddr.ip if conn.raddr else 'N/A'}:{conn.raddr.port if conn.raddr else 'N/A'}"
            status = conn.status
            pid = conn.pid
            print(f"Local Address: {local_address}, Remote Address: {remote_address}, Status: {status}, PID: {pid}")

if __name__ == "__main__":
    netstats = NetStats()
    netstats.print_net_connections()