from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader

from .models import Region
from .models import Role
from .models import Platform
from .models import Device
# Create your views here.

def index(request):
    region_list = Region.objects.all()
    device_role_list = Role.objects.all()
    device_platform_list = Platform.objects.all()
    device_list = Device.objects.all()
    template = loader.get_template('devices/index.html')
    context = RequestContext(request, {
        'region_list': region_list,
        'device_role_list': device_role_list,
        'device_platform_list': device_platform_list,
        'device_list': device_list,
    })
    return HttpResponse(template.render(context))
