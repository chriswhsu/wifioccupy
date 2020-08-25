from django.contrib import admin
from datapoll.models import *


# Register your models here.

class MACAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'mac_address', 'do_not_log']
    list_editable = ['do_not_log']


admin.site.register(MACAddress, MACAddressAdmin)


class MACAddressInline(admin.TabularInline):
    model = MACAddress


class WirelessDeviceAdmin(admin.ModelAdmin):
    list_display = ['mac_address', 'ip_address', 'hostname', 'alternative_name']
    list_editable = ['ip_address', 'hostname', 'alternative_name']


admin.site.register(WirelessDevice, WirelessDeviceAdmin)


class RouterAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'mac_24', 'ip_address_24', 'mac_50', 'ip_address_50']
    list_editable = ['mac_24', 'ip_address_24', 'mac_50', 'ip_address_50']


admin.site.register(Router, RouterAdmin)


class ChannelAdmin(admin.ModelAdmin):
    list_display = ['spectrum', 'channel_number', 'frequency', 'monitor']
    list_editable = ['monitor']


admin.site.register(Channel, ChannelAdmin)
