from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):

    return render(request, 'course/index.html', {"courses": Course.objects.all()})

def create(request):
	name_errors = Course.objects.basic_validator(request.POST)
	desc_errors = Description.objects.basic_validator(request.POST)
	if len(name_errors) and len(desc_errors):
		for key , value in name_errors.items():
			messages.error(request,value)
		for key , value in desc_errors.items():
			messages.error(request,value)	
		return redirect('/')
	else:
		Course.objects.create(name = request.POST['name'])
		course_id = Course.objects.get(name = request.POST['name'])
		Description.objects.create(Desc = request.POST['DESC'], course_desc=course_id)
		return redirect('/')

def destroy(request, id):

	return render(request, 'course/delete.html', {"course": Course.objects.get(id = id)})

def delete(request, id ):
	Course.objects.get(id = id).delete()
	return redirect('/')
