from django.urls import path
from baseapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("pdfview/", views.pdfview, name="pdfview"),
    path("pdfdownload/", views.pdfdownload, name="pdfdownload"),
    path("magazines/", views.magazines, name="magazines"),
    path("bookdownload/", views.bookdownload, name="bookdownload"),
    path("books/", views.books, name="books"),
    path("podcasts/", views.podcasts, name="podcasts"),
    path("listeners/<int:id>", views.listeners, name="listeners"),
    

]
