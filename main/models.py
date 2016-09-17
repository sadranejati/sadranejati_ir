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
    slug = models.SlugField(unique_for_month=date_published)
    published = models.BooleanField(default=True)

class comment(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField()
    url = models.URLField()
    content = models.TextField()
    comment_status_type = (('u','published'),('e','pending'),('d','deleted'))
    comment_status = models.CharField(max_length=3,choices=comment_status_type)
    reply = models.TextField(default=None)
    date_published = models.DateTimeField(auto_now_add=True,auto_now=False)
    date_answered = models.DateTimeField(auto_now=True,auto_now_add=False)

class category (models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField(unique=True)
    post = models.ManyToManyField(post)