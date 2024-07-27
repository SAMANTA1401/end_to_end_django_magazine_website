from django.shortcuts import render, redirect 
from django.contrib import messages
from blogapp.models import Blog , BlogComment
from blogapp.templatetags import extras
from django.http import HttpResponse,JsonResponse
from baseapp.models import WebCount



# Create your views here.

def bloginput(request):
    webcount = WebCount.objects.get()
    return render(request,'bloginput.html',{'wcount':webcount})

def blogsave(request):
    if request.method == 'POST':
            
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        email = request.POST.get('email')
        print(author)
        print(email)
        query = Blog(title=title, content=content, author=author, email=email)
        query.save()
        messages.success(request, 'Blog saved successfully')
        webcount = WebCount.objects.get()

        return render(request,'bloginput.html',{'wcount':webcount})

def blogview(request):
    blogs = Blog.objects.filter(admin_approved=True).order_by("pub_date")[::-1]
    webcount = WebCount.objects.get()
    return render(request, 'blogview.html', {'blogs': blogs,'wcount':webcount})


def blogread(request, id):
    print(id)
    blog = Blog.objects.filter(id=id).first()
    blog.views = blog.views + 1
    blog.save()

    comments= BlogComment.objects.filter(post=blog)
    webcount = WebCount.objects.get()
    
    context={
        'blog':blog,
        'comments': comments,
        'user': request.user,
        'wcount':webcount
    }
    return render(request, 'blogread.html', context)

def authorpage(request, author):
        blogs = Blog.objects.filter(author=author).order_by("pub_date")[::-1]
        webcount = WebCount.objects.get()
        return render(request, 'authorpage.html', {'blogs': blogs,'wcount':webcount})

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Blog.objects.get(id=postSno)
    
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")

        post.comments = post.comments + 1
        post.save()
       
    return redirect(f"/blogs/blogread/{post.id}")

def likescounter(request, id):
    blog = Blog.objects.get(id=id)
    blog.likes = blog.likes + 1
    blog.save()
    data={
        'like_count': str(blog.likes),
    }
    return JsonResponse(data)

def sharecounter(request, id):
    blog = Blog.objects.get(id=id)
    blog.share = blog.share + 1
    blog.save()
    data={
        'share_count': str(blog.share),
    }
    return JsonResponse(data)

    