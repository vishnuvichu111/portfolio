from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from .forms import LoginForm,BookCreateFrom
from .models import Book
from django.contrib.auth import authenticate,login


def home_view(request):
    return render(request, 'film/index.html')
def login_view(request):
    form = LoginForm()
    context = {}
    context["form"] = form


    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                if username == 'admin':
                    print("login Successfull")
                    login(request, user)
                    context = {}
                    ob1 = Book.objects.all()
                    context = {'data': ob1}
                    return render(request, 'film/userlogin.html', context)


    return render(request, 'film/login.html', context)


from django.shortcuts import render
def book_create(request):
    form=BookCreateFrom()
    context={}
    context["form"]=form
    books=Book.objects.all()
    context["books"]=books
    if request.method=='POST':
        form=BookCreateFrom(request.POST)
        if form.is_valid():
            form.save()
            print("book object seved")
            return redirect("create")

        else:
            print("else")
            form=BookCreateFrom(request.POST)
            context["form"]=form
            return render(request,'film/index.html',context)


    return render(request,'film/index.html',context)

from django.shortcuts import render

# Create your views here.
