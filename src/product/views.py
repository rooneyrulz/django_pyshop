from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from .models import Product
from .forms import ProductForm


def product_list_view(request):
	products = Product.objects.all()
	if len(products) < 1:
		context = {
			'title': 'Not Found!',
			'error_msg': 'No products found yet..'
		}
		return render(request, 'product/product_list.html', context)
	context = {
		'title': 'Products',
		'products': products
	}
	return render(request, 'product/product_list.html', context)


@staff_member_required()
def product_auth_list_view(request):
	products = Product.objects.filter(provider=request.user.id)
	if len(products) < 1:
		context = {
			'title': 'Not Found!',
			'error_msg': 'It seems you have not published any products yet..'
		}
		return render(request, 'product/product_auth_list.html', context)
	context = {
		'title': 'My Products',
		'products': products
	}
	return render(request, 'product/product_auth_list.html', context)


@staff_member_required()
def product_create_view(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.provider = request.user
		obj.save()
		messages.success(request, 'Product published successfully!')
		form = ProductForm()
	context = {
		'title': 'Create',
		'form': form
	}
	return render(request, 'product/product_create.html', context)


def product_details_view(request, id):
	product = get_object_or_404(Product, id=id)
	context = {
		'title': 'Details',
		'product': product
	}
	return render(request, 'product/product_details.html', context)


def product_edit_view(request, id):
	product = get_object_or_404(Product, id=id)
	context = {
		'title': 'Edit',
		'product': product
	}
	return render(request, 'product/product_edit.html', context)


def product_delete_view(request, id):
	product = get_object_or_404(Product, id=id)
	context = {
		'title': 'delete',
		'product': product
	}
	return render(request, 'product/product_delete.html', context)