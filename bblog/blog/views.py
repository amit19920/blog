# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog_Detail
def home_view(request,*args,**kwargs):
	for id in range(1,10):
		obj=Blog_Detail.objects.get(id=1)
		context={
		'title': obj.title,
		'description':obj.description,
		'time_now':obj.time_now
		}
	return render(request,'home.html' ,context)
	
def login_view(request,*args,**kwargs):
	return render(request,'login.html' ,{})
#def blog_detail(request):
	
#	return render(request,'detail.html',context) 

