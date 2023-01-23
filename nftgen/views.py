from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from cryptoaddress import get_crypto_address
from django.contrib.auth import authenticate, login, logout
import requests


# Create your views here.


def landing_view(request):
    return render(request, 'landing.html')


def logout_view(request):
    logout(request)
    return redirect(landing_view)


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        public_key = request.POST.get('public_key')
        verified = request.POST.get('verified')
        errors = []
        if verified == 'false':
            errors.append('Ethereum address NOT verified...')
            return render(request, 'login.html', {'errors': errors})

        try:
            eth_address = get_crypto_address('ETH', public_key)
            try:
                print(public_key)
                user = authenticate(username=public_key, password=public_key)
                if user is not None:
                    login(request, user)
                else:
                    errors.append(
                        'Account with this ethereum address does NOT exist...')
            except:
                errors.append(
                    'Account with this ethereum address does NOT exist...')
        except:
            errors.append(
                'Entered public address is NOT a valid ethereum address...')

        if len(errors) == 0:
            return redirect(landing_view)
        else:
            return render(request, 'login.html', {'errors': errors})


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        public_key = request.POST.get('public_key')
        email = request.POST.get('email')
        verified = request.POST.get('verified')
        errors = []
        if verified == 'false':
            errors.append('Ethereum address NOT verified...')
            return render(request, 'register.html', {'errors': errors})

        try:
            eth_address = get_crypto_address('ETH', public_key)
            try:
                user = User.objects.create_user(username=public_key,
                                                email=email,
                                                password=public_key)
                user = authenticate(username=public_key, password=public_key)
                if user is not None:
                    login(request, user)
            except:
                errors.append('Entered public address already exists...')
        except:
            errors.append(
                'Entered public address is NOT a valid ethereum address...')

        if len(errors) == 0:
            return redirect(landing_view)
        else:
            return render(request, 'register.html', {'errors': errors})


def artgen_view(request):
    if request.method == 'GET':
        return render(request, 'artgen.html')
    else:
        prompt = request.POST.get('prompt')
        accuracy = request.POST.get('accuracy')
        seed = None
        init_img = None
        img_strength = 0
        prompt_strength = 1.0

        iters = 50
        if accuracy == 'Low':
            iters = 25
        elif accuracy == 'Medium':
            iters = 50
        elif accuracy == 'High':
            iters = 100

        if request.POST.get('seed') != '':
            seed = int(request.POST.get('seed'))

        if request.POST.get('initimg') != '':
            init_img = request.POST.get('initimg')

        if request.POST.get('initimg') != '' and request.POST.get('img_strength') != '':
            img_strength = float(request.POST.get('img_strength'))
            prompt_strength = round(1 - img_strength, 1)

        url = 'https://replicate.delivery/pbxt/UWFTPVnSCDLNGNQ6P9if41gGhuOqHKk5q3IXsErwrUfEfJsgA/out-0.png'
        img = requests.get(url).content
        return render(request, 'art.html', {'img': img})


def art_view(request):
    return render(request, 'art.html')
