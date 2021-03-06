#wifitools.py

# Wifi connection and post functions for an ESP8266 board running micropython
#https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_basics.html

def connect(SSID,password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        #print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, password)
        while not sta_if.isconnected():
            pass
    #print('network config:', sta_if.ifconfig())
    return(sta_if)

def disconnect(sta_if):
    import network
    if sta_if.isconnected():
        sta_if.disconnect()
    if sta_if.active:
        sta_if.active(False)
    return


#https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_tcp.html
def http_get(url):
    import socket
    response =''
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            new = str(data, 'utf8')
            #print(str(data, 'utf8'), end='')
            response = response + new
        else:
            break
    return data


def thingspeak_post(API_key,data,field=1):
    if not isinstance(data, str):
        data = str(data)
    #base_url = 'https://api.thingspeak.com/update?api_key=THECLASSAPIKEY&field1=87'
    base_url = 'https://api.thingspeak.com/update?api_key='
    mid_url = '&field'
    field_num = str(field)
    url = base_url + API_key + mid_url +field_num + data
    response = http_get(url)
    return response
