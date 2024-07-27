from django.contrib import admin
from .models import *

# Register your models here.
class Magazinelist(admin.ModelAdmin):
    list_display = ['title','description','date']
admin.site.register(Magazine, Magazinelist)

class Booklist(admin.ModelAdmin):
    list_display = ['title','authname','date']
admin.site.register(Book,Booklist)

class Podlist(admin.ModelAdmin):
    list_display = ['title','authname','date']
admin.site.register(Podcast,Podlist)

class Wcount(admin.ModelAdmin):
    list_display = ['count']

admin.site.register(WebCount, Wcount)


