from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def landing_page_view(request):
	context = {
		'title': 'Landing'
	}
	return render(request, 'pages/landing_page.html', context)


@login_required()
def dashboard_page_view(request):
	context = {
		'title': 'Dashboard'
	}
	return render(request, 'pages/dashboard_page.html', context)


def about_page_view(request):
	context = {
		'title': 'About'
	}
	return render(request, 'pages/about_page.html', context)

