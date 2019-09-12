from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
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


@login_required()
def profile_edit_view(request):
	u_form = UserUpdateForm(request.POST or None, instance=request.user)
	p_form = ProfileUpdateForm(request.POST or None, request.FILES, instance=request.user.profile)

	if u_form.is_valid() and p_form.is_valid():
		u_form.save()
		p_form.save()
		messages.success(request, 'Profile has been successfully updated!')
		return redirect(f'/users/profile')

	context = {
		'title': 'Update',
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile_edit.html', context)


@login_required()
def profile_delete_view(request):
	profile = Profile.objects.get(user=request.user.id)
	if request.method == 'POST':
		profile.delete()
		messages.success(request, 'Profile has been successfully deleted!')
		return redirect('/users/profile')

	context = {
		'title': 'Delete',
		'profile': profile
	}
	return render(request, 'users/profile_delete.html', context)
