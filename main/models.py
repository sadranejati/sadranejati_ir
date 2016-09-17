# بسم الله الرحمن الرحیم
from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    post_type_choice = (('p','photo'),('b','blog'),('t','twitt'))
    title = models.CharField()
    content = models.TextField()
    photo = models.ImageField()
    date_published = models.DateTimeField(auto_now_add=True,auto_now=False)
    date_edited = models.DateTimeField(auto_now=True,auto_now_add=False)
    author = models.ForeignKey(User)
    post_type = models.CharField(choices=post_type_choice,max_length=1)
    can_send_comment = models.BooleanField(default=False)
    slug = models.SlugField()
    post_status_choice = (('pub','published'),('pen','pending'))
    status = models.CharField(max_length=3,choices=post_status_choice)