import random
import network
import espnow
import machine
import neopixel
import time

p = machine.Pin(4)
n = neopixel.NeoPixel(p, 60)

while True:
    for i in range(60):
        n[i] = (0, 0, 255)
    n.write()
    time.sleep(1)
    for i in range(60):
        n[i] = (255, 0, 0)
    n.write()
    time.sleep(1)


# Setup for the EspNow Protocol
# A WLAN interface must be active to send/recv
sta = network.WLAN(network.STA_IF)
sta.active(True)
print('Wlan Connection')

# Setup the EspNow network (Define Peers)
e = espnow.ESPNow()
e.active(True)
StartPort = b'\x34\x5F\x45\xAA\x25\x1C'
Portal_1 = b'\x34\x5F\x45\xAA\x98\xF4'
Portal_2 = b'\xD4\x8C\x49\x57\x4A\x3C'
Portal_3 = b'\x34\x5F\x45\xAA\xA3\xE4'
Portal_4 = b'\xD4\x8C\x49\x58\x4E\x58'
e.add_peer(StartPort)
e.add_peer(Portal_1)
e.add_peer(Portal_2)
e.add_peer(Portal_3)
e.add_peer(Portal_4)
print('EspNOW Set up :)')

e.send(Portal_1, 'Starting....')
e.send(Portal_2, 'Starting....')
e.send(Portal_3, 'Starting....')
e.send(Portal_4, 'Starting....')
e.send(Portal_5, 'Starting....')
e.send(Portal_6, 'Starting....')

# List of 4 portals
portals = [1, 2, 3, 4]
# Make a List of the random sequence of portals
randomPortals = []
# Make a var with the next portal in it
nextPortal = 0

# Function to say what portal is next
def whatportalnext(randomPortals):
    global nextPortal
    for i in range(4):
        if randomPortals[0] == i:
            nextPortal = i

# Custom shuffle function (like random.shuffle)
def custom_shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

#Start of Racing cycle::::::::::::::::::::::::::::::

def racingcycle():
    # Shuffle the list using the custom function
    custom_shuffle(portals)

    # Prints the full shuffled list
    print(portals)

    # readout the first number from the list and discarding it after
    whatportalnext(portals)
    portals.pop(0)

    # Send the remainder of the randomPortals list to the corresponding Portal MC
    if nextPortal == 1:
        e.send(Portal_1, str(portals).encode())
        print("Send to Portal 1")
    elif nextPortal == 2:
        e.send(Portal_2, str(portals).encode())
        print("Send to Portal 2")
    elif nextPortal == 3:
        e.send(Portal_3, str(portals).encode())
        print("Send to Portal 3")
    elif nextPortal == 4:
        e.send(Portal_4, str(portals).encode())
        print("Send to Portal 4")

    # Listen for a response back when the full sequence is complete to reset the program
    while True:
        host, msg = e.recv()
        if msg:
            print(host, msg)
            break

    print("NEXT ROUND!!!!!")

while True:
    racingcycle()