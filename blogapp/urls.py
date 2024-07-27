from django.urls import path
from blogapp import views

urlpatterns = [
    path("bloginput/",views.bloginput,name="bloginput"),
    path("blogsave/", views.blogsave,name= "blogsave"),
    path("blogview/", views.blogview,name= "blogview"),
    path("blogread/<int:id>", views.blogread,name= "blogread"),
    path("postComment", views.postComment, name="postComment"),
    path("likescounter/<int:id>", views.likescounter,name="likescounter"),
    path("sharecounter/<int:id>", views.sharecounter,name="sharecounter"),
    path("authorpage/<str:author>", views.authorpage,name="authorpage"),
]