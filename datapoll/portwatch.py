import socket
import logging as lgg
import hashlib

import datapoll.django_prep as ddp


from datapoll.models import WirelessDevice, PacketReceipt, Router, MACAddress

device_list = {}
UDP_IP = ddp.settings.LISTEN_UDP_IP
UDP_PORT = ddp.settings.LISTEN_UDP_PORT

lgg.basicConfig(level=lgg.INFO, format='%(asctime)s %(levelname)s %(message)s')

# This retrieves a Python logging instance (or creates it)
log = lgg.getLogger(__name__)

devices = WirelessDevice.objects.all()

for x in devices:
    device_list[x.mac_address.mac_address] = x.alternative_name

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # INTERNET  UDP
sock.bind((UDP_IP, UDP_PORT))
unique_list = {}

while True:
    received_bytes, addr = sock.recvfrom(1024)  # buffer size is 1024 received_bytes
    # decode byte string to string and
    data = received_bytes.decode("utf-8").rstrip('|').split(',')
    log.debug("received message: %s" % data)

    hexhash = hashlib.sha256(data[1].encode('utf-8')).hexdigest()

    mac, created = MACAddress.objects.get_or_create(mac_address_hash=hexhash,
                                                    mac_address=data[1])
    if created:
        lgg.info("Haven't see this mac address before, it's hash is {0}".format(hexhash))

    if mac.do_not_log:
        pass
    else:
        rss = data[2]

        rt = Router.objects.get(identifier=data[0])

        pr = PacketReceipt(mac_address=mac, router=rt, rss=rss)

        pr.save()
