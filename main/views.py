from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import post
# Create your views here.
def index(request):
    posts = post.objects.filter(published=True ).order_by('-date_published').all()
    return render(request,'main/index.html',{'site_config':settings.SITE_CONFIG,'posts':posts})