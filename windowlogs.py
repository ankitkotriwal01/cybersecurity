import platform
import win32evtlog
import win32evtlogutil
import os
import sys
import ctypes


def is_admin():
    """ Check if the script is running with admin privileges """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False


class WindowsLogs:
    def get_security_logs(self):
        if platform.system() != 'Windows':
            print('This program can only be run on Windows')
            return

        # Check for admin privileges
        if not is_admin():
            print("This script requires administrative privileges. Please run as administrator.")
            return

        # Open the Security event log
        try:
            handle = win32evtlog.OpenEventLog(None, "Security")
        except Exception as e:
            print(f"Error opening event log: {e}")
            return

        flags = win32evtlog.EVENTLOG_SEQUENTIAL_READ | win32evtlog.EVENTLOG_BACKWARDS_READ

        # Read events and display them
        try:
            while True:
                events = win32evtlog.ReadEventLog(handle, flags, 0)
                if not events:
                    break  # No more events to read

                for event_log in events:
                    log_message = win32evtlogutil.SafeFormatMessage(event_log, 'Security')
                    print(log_message)
        except Exception as e:
            print(f"Error reading event log: {e}")
        finally:
            win32evtlog.CloseEventLog(handle)  # Ensure the log is closed after reading


if __name__ == "__main__":
    logs = WindowsLogs()
    logs.get_security_logs()
