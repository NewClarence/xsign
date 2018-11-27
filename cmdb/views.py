# -*- coding: UTF-8 -*-

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from cmdb import forms, models



# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user_count = models.UserInfo.objects.filter(username=username).count()
            if user_count != 0:
                return render_to_response('cmdb/register.html', {'error': '用户名已存在'}, context_instance=RequestContext(request))
            else:
                password = form.cleaned_data['password']
                password2 = form.cleaned_data['password2']
                if password != password2:
                    return render_to_response('cmdb/register.html', {'error': '两次密码不一致'}, context_instance=RequestContext(request))
                else:
                    email = form.cleaned_data['email']
                    models.UserInfo.objects.create(username=username, password=password, email=email)
                    return render(request, 'cmdb/register_ok.html')
    else:
        form = forms.RegisterForm()
    return render(request, "cmdb/register.html", {"form": form})


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_count = models.UserInfo.objects.filter(username=username).count()
            if user_count == 0:
                return render_to_response('cmdb/login.html', {'error1': '用户名不存在'}, context_instance=RequestContext(request))
            else:
                user = models.UserInfo.objects.filter(username=username, password=password)
                if user:
                    return render_to_response('cmdb/success.html', {'username': username})
                else:
                    return render_to_response('cmdb/login.html', {'error2': '密码不正确'}, context_instance=RequestContext(request))
    else:
        form = forms.LoginForm()
    return render(request, 'cmdb/login.html', {'form': form})
