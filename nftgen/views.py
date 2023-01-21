from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from cryptoaddress import get_crypto_address
from django.contrib.auth import authenticate, login, logout

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
        print(request.POST)
        return render(request, 'artgen.html')
