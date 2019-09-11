from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
	# username = forms.CharField(
	# 	required=True,
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			'class': 'form-control form-control-lg',
	# 			'placeholder': 'Enter username'
	# 		}
	# 	)
	# )

	# email = forms.EmailField(
	# 	required=True,
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			'type': 'email',
	# 			'class': 'form-control form-control-lg',
	# 			'placeholder': 'Enter email'
	# 		}
	# 	)
	# )

	# password1 = forms.CharField(
	# 	required=True,
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			'type': 'password',
	# 			'class': 'form-control form-control-lg',
	# 			'placeholder': 'Enter password'
	# 		}
	# 	)
	# )

	# password2 = forms.CharField(
	# 	required=True,
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			'type': 'password',
	# 			'class': 'form-control form-control-lg',
	# 			'placeholder': 'Confirm password'
	# 		}
	# 	)
	# )

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password1',
			'password2'
		]
