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

# ### to turn on led over and over based on thingspeak:
# >>> for i in range(60*2):
# ...     r = get(url)
# ...     if r.text == '0':
# ...         led.off()
# ...     if r.text == '1':
# ...         led.on()
# ...     del r
# ...     time.sleep(5)
# ...
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Warning: getaddrinfo constraints not supported
# Traceback (most recent call last):
#   File "<stdin>", line 8, in <module>
# KeyboardInterrupt:
# >>> url
# 'https://api.thingspeak.com/channels/254616/fields/2/last'
# >>>
