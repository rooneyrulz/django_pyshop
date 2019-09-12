from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Profile

class RegisterForm(UserCreationForm):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control form-control-lg',
				'placeholder': 'Enter username'
			}
		)
	)

	email = forms.EmailField(
		widget=forms.TextInput(
			attrs={
				'type': 'email',
				'class': 'form-control form-control-lg',
				'placeholder': 'Enter email'
			}
		)
	)

	password1 = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'type': 'password',
				'class': 'form-control form-control-lg',
				'placeholder': 'Enter password'
			}
		)
	)

	password2 = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'type': 'password',
				'class': 'form-control form-control-lg',
				'placeholder': 'Confirm password'
			}
		)
	)

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password1',
			'password2'
		]



class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email']



class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['image']
