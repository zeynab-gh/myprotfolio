from pyexpat.errors import messages
from django.shortcuts import redirect, render,HttpResponse
from .models import Project,Category
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



def project_list(request):
    projects_all = Project.objects.all()
    
    return render(request, 'list.html', {'projects': projects_all})



def product(request,pk):
    product = Project.objects.get(id=pk)
    return render(request, 'product.html', {'project': product})


def category(request, cat):
    cat = cat.replace("-", " ")
    try:
        category = Category.objects.get(name=cat)
        products = Project.objects.filter(category=category)
        return render(request, 'category.html', {'projects': products, 'category': category})
    except Category.DoesNotExist:
        messages.error(request, 'دسته بندی وجود ندارد')
        return redirect("/")

def login_user(request):
    return render(request, 'html.login')


def logout_user(request):
    logout(request)
    messages.success(request,("با موفقیت خارج شدید"))
    return redirect("project_list")


def navbar(request):
    return render(request, 'navbar.html')

def heder(request):
    return render(request, 'heder.html')

def python(request):
    return render(request, 'python.html')

def django(request):
    return render(request, 'django.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render (request, 'contact.html')