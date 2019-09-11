# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		form.save()
		messages.success(request, f'User created successfully for {username}!')
		form = RegisterForm()

	context = {
		'title': 'User',
		'form': form
	}
	return render(request, 'users/register.html', context)
