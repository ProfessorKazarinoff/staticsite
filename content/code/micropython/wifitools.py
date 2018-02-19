
#https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_basics.html
def connect(SSID,password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

#https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_tcp.html
def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break

def thingspeak_post(API_key,data):
    if not isinstance(data, str):
        data = str(data)
    #base_url = 'https://api.thingspeak.com/update?api_key=THECLASSAPIKEY&field1=87'
    base_url = 'https://api.thingspeak.com/update?api_key='
    mid_url = '&field1='
    url = base_url + API_key + mid_url + data
    http_get(url)
