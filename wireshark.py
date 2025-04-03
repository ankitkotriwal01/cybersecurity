import pyshark


class WiresharkCapture:
    def do_capture(self):
        # Use PyShark to list available interfaces
        capture = pyshark.LiveCapture(interface=None)  # 'None' lets pyshark discover the default interface
        print("Available interfaces:")
        for iface in capture.interfaces:
            print(iface)

        # Choose the appropriate interface name based on your system
        interface = 'Wi-Fi'  # Update this based on your system's interface

        # Start the capture on the chosen interface
        capture = pyshark.LiveCapture(interface=interface)

        print(f"Capturing on interface: {interface}")

        # Capture 5 packets
        capture.sniff(packet_count=5)

        print(f"\nCaptured {len(capture)} packets")

        # Print packet details
        for packet in capture:
            print(f"\nPacket #{capture.index(packet)}:")
            print(packet)
            print(packet.summary())  # This will provide a summary of the packet

        # Optionally, print details of the first packet
        if len(capture) > 0:
            print("\nDetails of the first packet:")
            print(capture[0].summary())


if __name__ == "__main__":
    wireshark_capture = WiresharkCapture()
    wireshark_capture.do_capture()
