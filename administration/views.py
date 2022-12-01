from unittest import result
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from assessments.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from assessments.models import *
from administration.models import *

def staffLogin(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'stafflogin.html', context)

@staff_member_required
@login_required(login_url='login')
def dashboard(request):
	assessment =allAssessment.objects
	video = videoAns.objects.all()[:5]
	return render(request, 'dashboard.html',{'assessment':assessment, 'video':video})


@staff_member_required
@login_required(login_url='login')
def allAnswer(request):
	video = videoAns.objects.all()
	return render(request, 'allAnswer.html',{'video':video})


@staff_member_required
@login_required(login_url='login')
def searchbar(request):
	if request.method == 'GET':
		search = request.GET.get('search')
		result = videoAns.objects.all().filter(user_name = search)
	return render(request, 'searchbar.html',{'result':result})

