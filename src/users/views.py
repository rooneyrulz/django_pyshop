# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'User created successfully, You can now login!')
		return redirect('/users/login')

	context = {
		'title': 'User',
		'form': form
	}
	return render(request, 'users/register.html', context)
