from django.test import TestCase
from devices.models import Platform
from devices.models import Role 
from devices.models import Region
from devices.models import Device


# Create your tests here.

class Network(TestCase):
    def setup(self):
        Platform.objects.create(name='os_iosxr')
        Role.objects.create(name='provider_edge')
        Region.objects.create(name='dfw')
        Device.objects.create(name='pe1.dfw',
                              management_ip='10.0.0.1',
                              platform=Platform.objects.get(name='os_iosxr'),
                              role=Role.objects.get(name='provider_edge'),
                              region=Region.objects.get(name='dfw'))
