from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm

@staff_member_required()
def product_list_view(request):
	products = Product.objects.filter(provider=request.user.id)
	context = {
		'products': products
	}
	return render(request, 'product/product_list.html', context)


@staff_member_required()
def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.provider = request.user
		obj.save()
		form = ProductForm()
	context = {
		'form': form
	}
	return render(request, 'product/product_create.html', context)
