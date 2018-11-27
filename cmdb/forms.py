# -*- coding: UTF-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from cmdb import models
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, error_messages={'required': '用户不能为空'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), error_messages={'required': '密码不能为空'})
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(), error_messages={'required': '密码不能为空'})
    email = forms.EmailField(label='email', max_length=50, error_messages={'required': '邮箱不能为空'})

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, error_messages={'required': '用户不能为空'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), error_messages={'required': '密码不能为空'})
