from django.contrib import admin
from datapoll.models import *


# Register your models here.

class MACAddressAdmin(admin.ModelAdmin):
    list_display = ['mac_address']


admin.site.register(MACAddress, MACAddressAdmin)


class MACAdressInline(admin.TabularInline):
    model = MACAddress


class WirelessDeviceAdmin(admin.ModelAdmin):
    list_display = ['mac_address', 'ip_address', 'hostname', 'alternative_name']
