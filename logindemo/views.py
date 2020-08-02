from django.shortcuts import render, HttpResponse, redirect
from logindemo import models


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        ret = models.User.objects.filter(emails=email, password=password)
        if ret:
            # return HttpResponse('<h1>登录成功</h1>')
            # return HttpResponse('hello xad')
            return redirect('/index/')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def db_query(request):
    ret = models.User.objects.filter(emails='xad', password='xadxad')
    for i in ret:
        print(i, i.id, i.emails, i.password)
    # print(ret,type(ret))

    return HttpResponse('re')
# Create your views here.
