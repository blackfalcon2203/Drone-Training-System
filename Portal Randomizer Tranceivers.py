import network
import espnow
from hcsr04 import HCSR04

#set the pins for the ultrasonic sensor
ultrasone_sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

nextPortal = 0

def bytetostringconverter():
    global received_msg
    global randomPortals
    # decoding the incomming string back to a list:
    # Decode bytes to a string
    received_str = received_msg.decode()

    # Remove the brackets and split by commas to get individual items
    received_str = received_str.strip("[]")  # Remove the square brackets
    randomPortals = [int(x.strip()) for x in received_str.split(",")]  # Convert each item to an integer

    print(randomPortals)  # Output: [1, 2, 3, 4, 5]

# Function to say what portal is next
def whatportalnext(randomPortals):
    global nextPortal
    for i in range(6):
        if randomPortals[0] == i:
            nextPortal = i


# A WLAN interface must be active to send/recv
sta = network.WLAN(network.STA_IF)
sta.active(True)
print("WLAN Setup Complete :)")

# Set up the EspNow network (Define Peers)
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


def racingcycle():
    global received_msg
    while True:
        host, msg = e.recv()
        if msg:
            received_msg = msg
            break

    while True:
        distance = ultrasone_sensor.distance_cm()
        if distance < 30:
            break

    # readout the first number from the list and discarding it after
    whatportalnext(randomPortals)
    randomPortals.pop(0)

    # Send the remainder of the randomPortals list to the corresponding Portal MC
    if nextPortal == 1:
        e.send(Portal_1, str(randomPortals).encode())
        print("Send to Portal 1")
    elif nextPortal == 2:
        e.send(Portal_2, str(randomPortals).encode())
        print("Send to Portal 2")
    elif nextPortal == 3:
        e.send(Portal_3, str(randomPortals).encode())
        print("Send to Portal 3")
    elif nextPortal == 4:
        e.send(Portal_4, str(randomPortals).encode())
        print("Send to Portal 4")
    elif nextPortal == 5:
        e.send(Portal_5, str(randomPortals).encode())
        print("Send to Portal 5")
    elif nextPortal == 6:
        e.send(Portal_6, str(randomPortals).encode())
        print("Send to Portal 6")
    elif nextPortal == 0:
        e.send()

    print('Done!!!!!')

while True:
    racingcycle()