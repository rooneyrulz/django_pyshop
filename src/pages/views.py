from django.shortcuts import render


def landing_page_view(request):
	context = {
		'title': 'Landing'
	}
	return render(request, 'pages/landing_page.html', context)


def about_page_view(request):
	context = {
		'title': 'About'
	}
	return render(request, 'pages/about_page.html', context)

