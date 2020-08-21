from django.db import models


# Create your models here.

class MACAddress(models.Model):
    mac_address = models.CharField(max_length=17, unique=True, null=False)


class WirelessDevice(models.Model):
    mac_address = models.ForeignKey(MACAddress, on_delete=models.PROTECT)
    ip_address = models.CharField(max_length=15)
    hostname = models.CharField(max_length=30)
    alternative_name = models.CharField(max_length=30)


class Router(models.Model):
    identifier = models.CharField(max_length=4, null=False, unique=True)
    mac_24 = models.ForeignKey(MACAddress, related_name='mac_for_24_ghz', on_delete=models.PROTECT)
    ip_address_24 = models.CharField(max_length=15)
    mac_50 = models.ForeignKey(MACAddress, related_name='mac_for_50_ghz', on_delete=models.PROTECT)
    ip_address_50 = models.CharField(max_length=15)


class PacketReceipt(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    mac_address = models.ForeignKey(MACAddress, on_delete=models.PROTECT)
    router = models.ForeignKey(Router, on_delete=models.PROTECT)
    rss = models.SmallIntegerField()
