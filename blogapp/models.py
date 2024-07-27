from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django_summernote.fields import SummernoteTextField
from django.utils.timezone import now
from django.contrib.auth.models import User

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=225)
    content = models.TextField(null=True)
    author = models.CharField(max_length=225)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    email = models.EmailField(max_length=225)
    category=models.CharField(max_length=50,default='category')
    admin_approved = models.BooleanField(default=False)
    views= models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    # parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.post.title