import subprocess
import platform


class PingConnectivityOS:
    def check_ping_connectivity(self, host):
        try:
            # The commands line arguments are different based on the OS
            if platform.system() == 'Windows':
                # On Windows, we use -n to specify the number of ping requests
                result = subprocess.run(['ping', host, '-n', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                # On Unix-based systems (Linux/macOS), we use -c to specify the number of ping requests
                result = subprocess.run(['ping', host, '-c', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # If the ping command is successful, return True (host is up)
            if result.returncode == 0:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error occurred while pinging: {e}")
            return False


if __name__ == "__main__":
    ping_check_connectivity = PingConnectivityOS()
    status = ping_check_connectivity.check_ping_connectivity('thehappyfinance.com')

    if status:
        print("Host is up")
    else:
        print("Host is down")
