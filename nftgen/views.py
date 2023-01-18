from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from cryptoaddress import get_crypto_address
# Create your views here.


def landing_view(request):
    return render(request, 'landing.html')


def login_view(request):
    return render(request, 'login.html')


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
                                                password=email)
            except:
                errors.append('Entered public address already exists...')
        except:
            errors.append(
                'Entered public address is NOT a valid ethereum address...')

        if len(errors) == 0:
            return redirect(login_view)
        else:
            return render(request, 'register.html', {'errors': errors})
