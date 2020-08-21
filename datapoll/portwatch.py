import socket
from datetime import datetime
import logging as lgg

device_list = {
    'CC:95:D7:85:A1:1C': ['Vizio TV', 36],
    '58:6B:14:64:59:0E': ['ciphone10', '36'],
    'DC:A9:04:89:5A:1B': ['Chris-MBP-3', 36],
    '28:F0:76:09:DE:0C': ['CSM-iMac', 149],
    'D4:A3:3D:7A:3E:82': ['Living Room HomePod', 149],
    '14:D0:0D:AC:0E:17': ['Mielas-iPhone', '149'],
    'A4:F1:E8:90:44:A5': ['Stella-iPad', 149],
    'A4:83:E7:E1:CE:00': ['iMac2', 149],
    '34:A8:EB:25:5C:EB': ['Cats-iPad', 149],
    'F8:38:80:69:12:8C': ['S-iPhone', 149],
    'D4:A3:3D:83:1F:5E': ['CatPod', 157],
    'B4:18:D1:99:30:A7': ['iPad', '165'],

    'A4:CF:12:A0:16:FE': ['ESP_A016FE', 1],
    'F0:FE:6B:48:BA:B4': ['Shanghai 6303DF1', 1],
    '18:B4:30:09:78:7E': ['Nest', 1],
    'F8:6F:C1:42:3C:8B': ['ChrissApleWatch', 1],
    'AC:CF:23:ED:11:F8': ['Hi-Flyin-2C07676F93806C80', 11]

}

lgg.basicConfig(level=lgg.INFO, format='%(asctime)s %(levelname)s %(message)s')

# This retrieves a Python logging instance (or creates it)
log = lgg.getLogger(__name__)
UDP_IP = "192.168.1.210"
UDP_PORT = 5003

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # INTERNET  UDP
sock.bind((UDP_IP, UDP_PORT))
unique_list = {}

while True:
    bytes, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    # decode byte string to string and
    data = bytes.decode("utf-8").rstrip('|').split(',')
    log.debug("received message: %s" % data)

    source_lap = data[0]
    mac = data[1]
    timestamp = datetime.now()

    if mac in unique_list:
        unique_list[mac] = [unique_list[mac][0] + 1, timestamp, source_lap]
    else:
        unique_list.update({mac: [1, timestamp, source_lap]})
    log.info('--------------------------------')

    for x in unique_list:
        if x in device_list:
            string = str(device_list[x])
            log.info(string + ' ' + str(unique_list[x][0]) + ' ' + unique_list[x][2] + ' ' + unique_list[x][1].strftime("%m/%d/%Y, %H:%M:%S"))
