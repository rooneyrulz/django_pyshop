from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
	register_view, profile_view,
	profile_edit_view,
	profile_delete_view
)


urlpatterns = [
	path('register/', register_view, name='register_view'),
	path('profile/', profile_view, name='profile_view'),
	path('profile/edit/', profile_edit_view, name='profile_edit_view'),
	path('profile/delete/', profile_delete_view, name='profile_delete_view'),
	path('login/', LoginView.as_view(template_name='users/login.html'), name='login_view'),
	path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout_view')
]