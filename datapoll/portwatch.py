import socket
from datetime import datetime
import logging as lgg
import django
from django.conf import settings

import sys
import os

cur_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)))
base_dir = os.path.join(cur_dir, '..')
sys.path.extend([base_dir])

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wifioccupy.settings")
django.setup()

from datapoll.models import WirelessDevice, PacketReceipt, Router, MACAddress

device_list = {}
UDP_IP = "192.168.1.210"
UDP_PORT = 5003

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

    mac, created = MACAddress.objects.get_or_create(mac_address=data[1])
    rss = data[2]

    rt = Router.objects.get(identifier=data[0])

    pr = PacketReceipt(mac_address=mac, router=rt, rss=rss)

    pr.save()
