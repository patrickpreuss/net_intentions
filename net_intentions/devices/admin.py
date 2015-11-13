from django.contrib import admin
from .models import DeviceRole
from .models import DevicePlatform
from .models import Region
from .models import Device

# Register your models here.

admin.site.register(DeviceRole)
admin.site.register(DevicePlatform)
admin.site.register(Region)
admin.site.register(Device)
