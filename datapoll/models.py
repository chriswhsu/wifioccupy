from django.db import models


# Create your models here.

class MACAddress(models.Model):
    mac_address = models.CharField(max_length=17, unique=True, null=True, blank=True)
    mac_address_hash = models.CharField(max_length=64, unique=True, null=False)
    do_not_log = models.BooleanField(default=0)

    def __str__(self):
        return self.mac_address


class WirelessDevice(models.Model):
    mac_address = models.ForeignKey(MACAddress, on_delete=models.PROTECT)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    hostname = models.CharField(max_length=30, blank=True, null=True)
    alternative_name = models.CharField(max_length=30)


class Router(models.Model):
    identifier = models.CharField(max_length=4, null=False, unique=True)
    mac_24 = models.ForeignKey(MACAddress, related_name='mac_for_24_ghz', on_delete=models.PROTECT, blank=True,
                               null=True)
    ip_address_24 = models.CharField(max_length=15, blank=True, null=True)
    mac_50 = models.ForeignKey(MACAddress, related_name='mac_for_50_ghz', on_delete=models.PROTECT, blank=True,
                               null=True)
    ip_address_50 = models.CharField(max_length=15, blank=True, null=True)


class PacketReceipt(models.Model):
    packet_datetime = models.DateTimeField(auto_now_add=True, primary_key=True)
    mac_address = models.ForeignKey(MACAddress, on_delete=models.PROTECT)
    router = models.ForeignKey(Router, on_delete=models.PROTECT)
    rss = models.SmallIntegerField()

    class Meta:
        managed = False


class Channel(models.Model):
    channel_number = models.SmallIntegerField(primary_key=True)

    SPECTRA = ((50, "5 GHz"),
               (24, "2.4 GHz"))

    spectrum = models.SmallIntegerField(choices=SPECTRA)
    frequency = models.SmallIntegerField()
    monitor = models.BooleanField(default=0)
