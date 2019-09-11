from django.urls import path

from .views import product_list_view, product_details_view, product_create_view, product_auth_list_view, product_edit_view, product_delete_view 

app_name = 'product'
urlpatterns = [
	path('', product_list_view, name='product_list_view'),
	path('details/<int:id>/', product_details_view, name='product_details_view'),
	path('details/<int:id>/edit/', product_edit_view, name='product_edit_view'),
	path('details/<int:id>/delete/', product_delete_view, name='product_delete_view'),
	path('my-product/', product_auth_list_view, name='product_auth_list_view'),
	path('create/', product_create_view, name='product_create_view')
]