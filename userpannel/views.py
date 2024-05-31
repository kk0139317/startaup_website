from django.shortcuts import render, redirect
from userpannel.models import ContactForm
# Create your views here.

def HomePage(request):
    return render(request, 'userpannel/index.html')

def AboutUs(request):
    data = {'index':'', 'about':'active', 'service':'', 'blog':'', 'pages':'', 'contact':'', 'title':"About Us"}
    return render(request, 'userpannel/about.html', data)

def ServicePage(request):
    data = {'index':'', 'about':'', 'service':'active', 'blog':'', 'pages':'', 'contact':'', 'title':"Services"}
    return render(request, 'userpannel/service.html', data)

def Contact(request):
    data = {'index':'', 'about':'', 'service':'', 'blog':'', 'pages':'', 'contact':'active', 'title':"Contact"}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = ContactForm(name=name, email=email, subject=subject, message=message)
        contact.save()
        return redirect("/")
    else:
        return render(request, 'userpannel/contact.html', data)
    
def Team(request):
    return render(request, 'userpannel/team.html',{'title':"Team Memeber"})


def Blog(request):
    return render(request, 'userpannel/blog.html',{'title':"Blog"})

def Detail(request):
    return render(request, 'userpannel/detail.html', {'title':"Blog Detal"})