from django.shortcuts import render

# Create your views here.


def landing_view(request):
    return render(request, 'landing.html')


def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')
