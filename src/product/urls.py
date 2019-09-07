from django.urls import path

from .views import product_list_view, product_details_view, product_create_view, product_auth_list_view


app_name = 'product'
urlpatterns = [
	path('', product_list_view, name='product_list_view'),
	path('details/<int:id>/', product_details_view, name='product_details_view'),
	path('my-product/', product_auth_list_view, name='product_auth_list_view'),
	path('create/', product_create_view, name='product_create_view')
]