# بسم الله الرحمن الرحیم
from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class post(models.Model):
    post_type_choice = (('p','photo'),('b','blog'),('t','twitt'))
    title = models.CharField(max_length=125,blank=True)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    date_published = models.DateTimeField(auto_now_add=True,auto_now=False)
    date_edited = models.DateTimeField(auto_now=True,auto_now_add=False)
    author = models.ForeignKey(User)
    post_type = models.CharField(choices=post_type_choice,max_length=1)
    can_send_comment = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,blank=True)
    published = models.BooleanField(default=True)
    category = models.ManyToManyField(category)
    def __str__(self):
        if self.title:
            return self.title
        else:
            if self.post_type == 't':
                return "twitt"
            else:
                return "photo"

class comment(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField()
    url = models.URLField(blank=True)
    content = models.TextField()
    comment_status_type = (('u','published'),('e','pending'),('d','deleted'))
    comment_status = models.CharField(max_length=3,choices=comment_status_type)
    reply = models.TextField(blank=True)
    date_published = models.DateTimeField(auto_now_add=True,auto_now=False)
    date_answered = models.DateTimeField(auto_now=True,auto_now_add=False)
    post = models.ForeignKey(post,default=None)
    def __str__(self):
        return self.name+" "+self.post.title

