from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Profile


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



@login_required()
def profile_view(request):
	try:
		profile = Profile.objects.get(user=request.user.id)
	except Profile.DoesNotExist:
		context = {
			'title': 'Profile'
		}
		return render(request, 'users/profile.html', context)

	context = {
		'title': 'Profile',
		'profile': profile
	}
	return render(request, 'users/profile.html', context)
