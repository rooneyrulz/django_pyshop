from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
	name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'id': 'name',
				'class': 'form-control',
				'placeholder': 'Enter name'
			}
		)
	)

	price = forms.DecimalField(
		widget=forms.NumberInput(
			attrs={
				'id': 'price',
				'class': 'form-control',
				'placeholder': 'Enter price'
			}
		)
	)

	description = forms.CharField(
		required=False,
		widget=forms.Textarea(
			attrs={
				'id': 'description',
				'class': 'form-control',
				'placeholder': 'Enter description',
				'rows': 4
			}
		)
	)

	class Meta:
		model = Product
		fields = [
			'name',
			'price',
			'description',
			'image'
		]
