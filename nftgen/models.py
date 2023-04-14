from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Digital_Art(models.Model):
    init_image = models.ImageField(upload_to='initial_images/', blank=True,
                                   default='default-noise_ea8wzb.png')
    gen_image = models.ImageField(
        upload_to='generated_images/', blank=False, null=False)
    prompt = models.TextField(blank=False, null=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='digital_art', blank=False, null=False)
    iterations = models.IntegerField(blank=False, null=False)
    image_strength = models.DecimalField(
        max_digits=2, decimal_places=1, blank=False, null=False)
    run_time = models.IntegerField(blank=False, null=False)
    timestamp = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    seed = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Digital_Art'
        verbose_name_plural = 'Digital_Art'


class NFT_Collection(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='collection', blank=False, null=False)
    contract_address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='collection_logos/', blank=False, null=False,
                             default='default-collection_dfbpsd.jpg')

    class Meta:
        verbose_name = 'NFT_Collection'
        verbose_name_plural = 'NFT_Collection'


class NFT(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='nft', blank=False, null=False)
    contract_address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=200)
    token_id = models.CharField(
        max_length=100, blank=False, null=False, default='0')

    class Meta:
        verbose_name = 'NFT'
        verbose_name_plural = 'NFT'


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=False, null=False,
                                    default='default-profile-pic_itkdbu.png')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
