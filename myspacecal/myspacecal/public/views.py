# myspacecal.public.views
# encoding=utf-8

from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.timezone import utc


def home(request):
    ctx = {}
    return TemplateResponse(request, 'public/base_home.html', ctx)

def about(request):
    ctx = {}
    return TemplateResponse(request, 'public/base_about.html', ctx)

def contact (request):
    ctx = {}
    return TemplateResponse(request, 'public/base_contact.html', ctx)
