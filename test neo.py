import neopixel
import machine
import time
import espnow
imo

p = machine.Pin(4)
n = neopixel.NeoPixel(p, 60)

while True:
    for i in range(60):
        n[i] = (0, 0, 255)
    n.write()
    time.sleep(1)
    for i in range(60):
        n[i] = (255, 100, 0)
    n.write()
    time.sleep(1)
