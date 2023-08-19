from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    points = models.IntegerField(default=0)
    spins_left = models.IntegerField(default=3)  # Number of spins user has left

    def __str__(self):
        return self.username

class Prize(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='prize_images/')
    quantity = models.IntegerField(default=0)  # Number of available prizes

    def __str__(self):
        return self.name

class Spin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.prize.name} - Winner: {self.is_winner}"
