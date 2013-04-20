# myspacecal.public.views
# encoding=utf-8

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils.timezone import utc
from myspacecal.data.models import Agency
from myspacecal.data.models import Satellite

agencies = Agency.objects.all()
satellites = Satellite.objects.all()

COMMON_CONTEXT = {
    'agencies': agencies,
    'satellites': satellites,
}

def home(request):
    ctx = {
    }
    ctx = dict(COMMON_CONTEXT, **ctx)
    return TemplateResponse(request, 'public/base_home.html', ctx)

def about(request):
    ctx = {}
    ctx = dict(COMMON_CONTEXT, **ctx)
    return TemplateResponse(request, 'public/base_about.html', ctx)

def contact(request):
    ctx = {}
    ctx = dict(COMMON_CONTEXT, **ctx)
    return TemplateResponse(request, 'public/base_contact.html', ctx)

def help(request):
    ctx = {}
    ctx = dict(COMMON_CONTEXT, **ctx)
    return TemplateResponse(request, 'public/base_help.html', ctx)

def agency(request, slug):
    agency = get_object_or_404(Agency, slug=slug)
    ctx = {
        'agency': agency,
    }
    ctx = dict(COMMON_CONTEXT, **ctx)
    return TemplateResponse(request, 'public/base_agency.html', ctx)

def satellite(request, slug):
    satellite = get_object_or_404(Satellite, slug=slug)
    ctx = {
        'satellite': satellite,
    }
    ctx = dict(COMMON_CONTEXT, **ctx)
    return TemplateResponse(request, 'public/base_satellite.html', ctx)
