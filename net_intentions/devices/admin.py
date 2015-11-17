from django.contrib import admin
from .models import Role
from .models import Platform
from .models import Region
from .models import Device

# Register your models here.

admin.site.register(Role)
admin.site.register(Platform)
admin.site.register(Region)
admin.site.register(Device)
