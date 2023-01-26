from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Digital_Art(models.Model):
    init_image = models.ImageField(upload_to='initial_images/', blank=True,
                                   default='initial_images/default-noise.png')
    gen_image = models.ImageField(upload_to='generated_images/', blank=False)
    prompt = models.TextField(blank=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='digital_art', blank=False)
    iterations = models.IntegerField(blank=False)
    image_strength = models.DecimalField(
        max_digits=2, decimal_places=1, blank=False)
    run_time = models.IntegerField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Digital_Art'
        verbose_name_plural = 'Digital_Art'
