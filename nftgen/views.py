from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from cryptoaddress import get_crypto_address
from django.contrib.auth import authenticate, login, logout
from .models import Digital_Art, Profile, NFT_Collection, NFT
import requests
from django.core.files.base import ContentFile
import time
import replicate
import tempfile
from deepmint.local_settings import BASE_DIR
import os
from PIL import Image
from dotenv import load_dotenv
import json
import requests
from django.http import JsonResponse
from urllib.parse import unquote
from django.contrib.auth.decorators import login_required
load_dotenv()

# Create your views here.


def landing_view(request):
    DEEPMINT_NFT_ADDRESS = os.environ.get('DEEPMINT_NFT_ADDRESS')
    return render(request, 'landing.html', {"deepmint_nft_address": DEEPMINT_NFT_ADDRESS})


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


def resize_image(input_image_file):
    original_image = Image.open(input_image_file.name)
    resized_image = original_image.resize((768, 768)).convert('RGB')
    input_image_file.close()
    os.remove(input_image_file.name)
    output_img_file = tempfile.NamedTemporaryFile(
        delete=False, dir=os.path.join(BASE_DIR, 'nftgen', 'temp'), suffix=".jpg")

    resized_image.save(output_img_file, format='JPEG')
    output_img_file.close()
    return output_img_file


def generate_art(prompt, prompt_strength, init_image, seed, iters):
    model = replicate.models.get("stability-ai/stable-diffusion-img2img")
    version = model.versions.get(
        "15a3689ee13b0d2616e98820eca31d4c3abcd36672df6afce5cb6feb1d66087d")

    init_img_file = tempfile.NamedTemporaryFile(
        delete=False, dir=os.path.join(BASE_DIR, 'nftgen', 'temp'))

    for chunk in init_image.chunks():
        init_img_file.write(chunk)

    init_img_file = resize_image(init_img_file)

    inputs = {
        'prompt': prompt,
        'image': open(init_img_file.name, "rb"),
        'prompt_strength': prompt_strength,
        'num_outputs': 1,
        'num_inference_steps': iters,
        'guidance_scale': 7.5,
        'scheduler': "DPMSolverMultistep",
    }
    if seed is not None:
        inputs['seed'] = seed

    gen_img_url = version.predict(**inputs)[0]
    init_img_file.close()

    return gen_img_url, init_img_file


def create_new_art(init_img, digital_art, art_num):
    digital_art.init_image.save(
        'initimg-'+str(art_num)+'.png', init_img)


@login_required
def artgen_view(request):
    if request.method == 'GET':
        return render(request, 'artgen.html')
    else:
        prompt = request.POST.get('prompt')
        quality = request.POST.get('quality')
        seed = None
        init_img = None
        img_strength = 0
        prompt_strength = 1.0

        iters = 50
        if quality == 'Low':
            iters = 25
        elif quality == 'Medium':
            iters = 50
        elif quality == 'High':
            iters = 100

        if request.POST.get('seed') != '':
            seed = int(request.POST.get('seed'))

        if 'initimg' in request.FILES:
            init_img = request.FILES['initimg']

        if 'initimg' in request.FILES and request.POST.get('img_strength') != '':
            img_strength = float(request.POST.get('img_strength'))
            prompt_strength = round(1 - img_strength, 1)

        art_num = Digital_Art.objects.count() + 1

        digital_art = Digital_Art(owner=request.user, iterations=iters,
                                  image_strength=img_strength, prompt=prompt,
                                  seed=seed)

        start_time = time.time()
        img_url, init_img_file = generate_art(prompt, prompt_strength,
                                              digital_art.init_image, seed, iters)
        end_time = time.time()

        run_time = end_time - start_time
        digital_art.run_time = run_time

        gen_img = requests.get(img_url).content
        gen_img = ContentFile(gen_img, name='genimg-'+str(art_num)+'.png')

        digital_art.gen_image.save(
            'genimg-'+str(art_num)+'.png', gen_img)

        if 'initimg' in request.FILES:
            create_new_art(init_img, digital_art, art_num)

        os.remove(init_img_file.name)
        digital_art.save()
        return redirect(art_view, digital_art.id)


@login_required
def art_view(request, id):
    art = Digital_Art.objects.filter(id=id).first()
    gen_img_path = os.path.basename(art.gen_image.url)
    return render(request, 'art.html', {'art': art, 'gen_img_path': gen_img_path})


@login_required
def profile_view(request):
    if request.method == 'GET':
        art = Digital_Art.objects.filter(owner=request.user)
        collections = NFT_Collection.objects.filter(owner=request.user)
        nfts = NFT.objects.filter(owner=request.user)
        return render(request, 'profile.html', {'digital_art': art,
                                                'nft_collections': collections,
                                                'nfts': nfts})

    elif 'updateprofile' in request.POST:
        if 'profilepic' in request.FILES:
            profile_pic = request.FILES['profilepic']
            profile = Profile.objects.update_or_create(user=request.user,
                                                       defaults={'profile_pic': profile_pic})
        return redirect(profile_view)

    elif request.is_ajax():
        name = request.POST.get('name')
        symbol = request.POST.get('symbol')
        contract_address = request.POST.get('contract_address')
        # create new instance of NFTCollection model
        if 'logo' in request.FILES:
            logo = request.FILES.get('logo')
            nft_collection = NFT_Collection(
                name=name, symbol=symbol, contract_address=contract_address,
                owner=request.user, logo=logo)
            nft_collection.save()
        else:
            nft_collection = NFT_Collection(
                name=name, symbol=symbol, contract_address=contract_address,
                owner=request.user)
            nft_collection.save()
        return JsonResponse({'status': 'success'})


@login_required
def nftgen_view(request, art_id=None):
    if request.method == 'GET':
        PINATA_API_KEY = os.environ.get('PINATA_API_KEY')
        PINATA_API_SECRET = os.environ.get('PINATA_API_SECRET')
        DEEPMINT_NFT_ADDRESS = os.environ.get('DEEPMINT_NFT_ADDRESS')

        gen_img_path = ''
        description = ''

        collections = NFT_Collection.objects.filter(owner=request.user)
        art = Digital_Art.objects.filter(id=art_id).first()

        if art:
            description = art.prompt
            gen_img_path = art.gen_image.url

        return render(request, 'nftgen.html', {'nft_collections': collections,
                                               'nft_description': description,
                                               'nft_image': gen_img_path,
                                               'pinata_api_key': PINATA_API_KEY,
                                               'pinata_api_secret': PINATA_API_SECRET,
                                               'deepmint_nft_address': DEEPMINT_NFT_ADDRESS})

    elif request.is_ajax():
        name = request.POST.get('name')
        desc = request.POST.get('description')
        contract_address = request.POST.get('contract_address')
        nft_img_url = request.POST.get('image_url')
        tokenid = request.POST.get('tokenid')
        nft = NFT(
            name=name, description=desc, contract_address=contract_address,
            owner=request.user, image_url=nft_img_url, token_id=tokenid)
        nft.save()
        return JsonResponse({'status': 'success'})

    else:
        return render(request, 'nftgen.html')
