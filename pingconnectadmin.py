from pythonping import ping

class PingConnectivity:
    def check_ping_connectivity(self, host: str) -> bool:
        try:
            response = ping(host, verbose=True)
            if response.success():
                print(f"Ping to {host} successful!")
                return True
            else:
                print(f"Ping to {host} failed.")
                return False
        except Exception as e:
            print(f"Error pinging {host}: {e}")
            return False


if __name__ == "__main__":
    ping_check_connectivity = PingConnectivity()
    success = ping_check_connectivity.check_ping_connectivity('thehappyfinance.com')
    if success:
        print("Google is reachable!")
    else:
        print("Google is not reachable.")
