from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'main/index.html',{'site_config':settings.SITE_CONFIG})