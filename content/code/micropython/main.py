# main.py
# ESP8266 Feather Huzzah Weather Station

import wifitools
import MCP9808
import time
import config

api_key = config.API_KEY
ssid = config.SSID
password = config.WIFI_PASSWORD

for i in range(12*60):
    sta_if = wifitools.connect(ssid, password)
    time.sleep(5)
    data = MCP9808.readtemp()
    wifitools.thingspeak_post(api_key,data)
    wifitools.disconnect(sta_if)
    time.sleep(55)
