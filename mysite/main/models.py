from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Game(models.Model):
    title = models.CharField(max_length=100)
    img1 = models.ImageField(default='default.png', upload_to='game_pics')
    img2 = models.ImageField(default='default.png', upload_to='game_pics')
    data = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game-detail', kwargs={'pk': self.pk})


# Create your models here.
