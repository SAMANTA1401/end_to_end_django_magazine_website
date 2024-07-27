from django.contrib import admin
from .models import Blog , BlogComment

from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget 
from django.db import models




class SummerBlog(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ['title','author','pub_date']

admin.site.register(Blog, SummerBlog )

# class QuestionAdmin(admin.ModelAdmin): 

#      formfield_overrides = { 
#             models.TextField: {'widget': SummernoteWidget}, 
#      } 

# admin.site.register(Blog,QuestionAdmin)

class CommentList(admin.ModelAdmin):
    list_display = ['post','user','timestamp']

admin.site.register(BlogComment, CommentList)