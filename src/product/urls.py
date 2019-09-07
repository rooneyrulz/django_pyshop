from django.urls import path

from .views import product_create_view, product_list_view


app_name = 'product'
urlpatterns = [
	path('', product_list_view, name='product_list_view'),
	path('create/', product_create_view, name='product_create_view')
]