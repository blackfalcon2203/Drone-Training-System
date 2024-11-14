import network
import ubinascii

wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)
wlan_mac = wlan_sta.config('mac')

print(ubinascii.hexlify(wlan_mac, ':').decode().upper())
print(':)')