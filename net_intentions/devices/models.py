from django.db import models

# Create your models here.

class DeviceRole(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class DevicePlatform(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255, unique=True)
    management_ip = models.GenericIPAddressField(unpack_ipv4=False,
                                                 unique=True)
    device_platform = models.ForeignKey('DevicePlatform')
    device_role = models.ForeignKey('DeviceRole')
    region = models.ForeignKey('Region')

    def __str__(self):
        return self.name
