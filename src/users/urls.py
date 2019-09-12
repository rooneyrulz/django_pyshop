from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import register_view


urlpatterns = [
	path('register/', register_view, name='register_view'),
	path('login/', LoginView.as_view(template_name='users/login.html'), name='login_view'),
	path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout_view')
]