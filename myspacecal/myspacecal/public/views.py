# myspacecal.public.views
# encoding=utf-8

from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.timezone import utc
from myspacecal.data.models import Agency
from myspacecal.data.models import Satellite


def home(request):
    ctx = {
        'agencies': Agency.objects.all(),
        'satellites': Satellite.objects.all(),
    }
    return TemplateResponse(request, 'public/base_home.html', ctx)

def about(request):
    ctx = {}
    return TemplateResponse(request, 'public/base_about.html', ctx)

def contact (request):
    ctx = {}
    return TemplateResponse(request, 'public/base_contact.html', ctx)

def agency(request, slug):
    agency = Agency.objects.get_object_or_404(slug=slug)
    ctx = {
        'agency': agency,
    }
    return TemplateResponse(request, 'public/base_agency.html', ctx)

def satellite(request, slug):
    satellite = Satellite.objects.get_object_or_404(slug=slug)
    ctx = {
        'satellite': satellite,
    }
    return TemplateResponse(request, 'public/base_satellite.html', ctx)
