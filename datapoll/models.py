from django.db import models

# Create your models here.


class MACAddress(models.Model):

    mac_address = models.CharField(max_length=17, unique=True, null=False)
    ip_address = models.CharField(max_length=15)
    hostname = models.CharField(max_length=30)
    alternative_name = models.CharField(max_length=30)
