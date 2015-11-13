from django.db import models

# Create your models here.

class DeviceRole(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    role = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.role


class DevicePlatform(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    platform = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.platform


class Region(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    region = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.region


class Device(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    hostname = models.CharField(max_length=255, unique=True)
    management_ip = models.GenericIPAddressField(unpack_ipv4=False)
    device_platform = models.ForeignKey('DevicePlatform')
    device_role = models.ForeignKey('DeviceRole')
    region = models.ForeignKey('Region')

    def __str__(self):
        return self.hostname
