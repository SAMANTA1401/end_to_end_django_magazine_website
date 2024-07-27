from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Magazine , Book , Podcast, WebCount
import base64
from pathlib import Path
from django.core.files import File
from  io import BytesIO
from django.contrib import messages
from blogapp.models import Blog, BlogComment 
from django.conf import settings
import os
from dotenv import load_dotenv
from baseapp.get_para import get_parameter
import boto3

load_dotenv()

# Create your views here.
def home(request):
    magazines = Magazine.objects.all()[::-1][:5]
    lastmagazine = Magazine.objects.all().order_by("date")[::-1][:1]
    blogs = Blog.objects.filter(admin_approved=True).order_by("pub_date")[::-1][:4]
    popblogs = Blog.objects.filter(admin_approved=True).order_by('views')[::-1][:4]
    books = Book.objects.all().order_by('download')[::-1][:4]
    webcount = WebCount.objects.get()
    webcount.count = webcount.count + 1
    webcount.save()
    context = {
        'magazines':magazines,
        'lastmag':lastmagazine,
        'blogs':blogs,
        "popblogs":popblogs,
        "books":books,
        'media_url':settings.MEDIA_URL,
        'wcount':webcount,
        }
    
    return render(request, 'home.html',context=context)

def magazines(request):
    magazines = Magazine.objects.all().order_by("date")[::-1]
    webcount = WebCount.objects.get()
    context = {'magazines':magazines,'wcount':webcount}
    return render(request,'magazine.html',context=context)


def pdfview(request):
    if request.method == 'POST':
        pdffile = request.POST.get('pdffile')
        pdf_inst=Magazine.objects.get(pdffile=pdffile)
        pdf_inst.read = pdf_inst.read + 1
        pdf_inst.save()

        file = f'media/{pdffile}'
        s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID , aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, region_name=settings.AWS_S3_REGION_NAME)
    
        response = s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file)
        bytesdata = response['Body'].read()

        # path = pdf_inst.pdffile.path
        # f = open(path, "rb")
        # myfile = File(f)
        # bytesdata=myfile.read()

        pdf_data_base64 = base64.b64encode(bytesdata).decode('utf-8')
        # adobeclient = os.environ['ADOBE_CLIENT_ID']
        adobeclient = get_parameter('/anneshon/google/clientid')

        return render(request, 'pdfview.html',{'pdf_data_base64': pdf_data_base64,"filename":pdffile, "adobeclient":adobeclient})

    return HttpResponse("pdfview not working")


def pdfdownload(request):
    if request.method == 'POST':
        pdffile = request.POST.get('pdffile')
        pdf_inst=Magazine.objects.get(pdffile=pdffile)
        pdf_inst.download = pdf_inst.download + 1
        pdf_inst.save()

        file = f'media/{pdffile}'
        s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID , aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, region_name=settings.AWS_S3_REGION_NAME)
    
        response = s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file)
        bytesdata = response['Body'].read()

        # path = pdf_inst.pdffile.path
        # print(path)
        # f = open(path, "rb")
        # myfile = File(f)
        # bytesdata=myfile.read()

        responses = HttpResponse(BytesIO(bytesdata),content_type='application/pdf')
        responses['Content-Disposition'] = f'attachment; filename={pdffile}'
        
        return responses

def bookdownload(request):
    if request.method == 'POST':
        bookfile = request.POST.get('bookfile')
        book_inst=Book.objects.get(pdf=bookfile)
        book_inst.download = book_inst.download + 1
        book_inst.save()

        file = f'media/{bookfile}'
        s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID , aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, region_name=settings.AWS_S3_REGION_NAME)
    
        response = s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file)
        bytesdata = response['Body'].read()
        
        # path = book_inst.pdf.url
        # print(path)
        # f = open(path, "rb")
        # myfile = File(f)
        # bytesdata=myfile.read()

        responses = HttpResponse(BytesIO(bytesdata), content_type='application/pdf')
        responses['Content-Disposition'] = f'attachment; filename={bookfile}'
        return responses


def books(request):
    books = Book.objects.all().order_by('download')[::-1]
    webcount = WebCount.objects.get()
    context={
        'books':books,
        'wcount':webcount
    }
    return render(request, 'book.html', context=context)

def podcasts(request):
    podcasts = Podcast.objects.all().order_by('date')[::-1]
    webcount = WebCount.objects.get()
    context={
        'podcasts':podcasts,
        'wcount':webcount

    }
    return render(request, 'podcasts.html',context=context)

def listeners(request,id):
    podcast = Podcast.objects.get(id=id)
    podcast.listener = podcast.listener + 1
    podcast.save()
    data={
        'listeners': str(podcast.listener),
    }
    return JsonResponse(data)
    