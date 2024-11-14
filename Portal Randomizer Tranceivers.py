import network
import espnow

# A WLAN interface must be active to send/recv
sta = network.WLAN(network.STA_IF)
sta.active(True)
print("WLAN Setup Complete :)")

# Setup the EspNow network (Define Peers)
e = espnow.ESPNow()
e.active(True)
StartPort = b'\x34\x5F\x45\xAA\x25\x1C'
Portal_1 = b'\x34\x5F\x45\xAA\x98\xF4'
Portal_2 = b'\xD4\x8C\x49\x57\x4A\x3C'
Portal_3 = b'\x34\x5F\x45\xAA\xA3\xE4'
Portal_4 = b'\xD4\x8C\x49\x58\x4E\x58'
Portal_5 = b'\xD4\x8C\x49\x57\x0D\x78'
Portal_6 = b'\xD4\x8C\x49\x57\x15\xAC'
e.add_peer(StartPort)
e.add_peer(Portal_1)
e.add_peer(Portal_2)
e.add_peer(Portal_3)
e.add_peer(Portal_4)
e.add_peer(Portal_5)
e.add_peer(Portal_6)
print("EspNow Setup complete :)")

while True:
    host, msg = e.recv()
    if msg:
        print(host, msg)
        if msg == b'end':
            break




# decoding the incomming string back to a list:
# Example received message as bytes
received_message = b"[1, 2, 3, 4]"

# Decode bytes to a string
received_str = received_message.decode()

# Remove the brackets and split by commas to get individual items
received_str = received_str.strip("[]")  # Remove the square brackets
received_list = [int(x.strip()) for x in received_str.split(",")]  # Convert each item to an integer

print(received_list)  # Output: [1, 2, 3, 4]