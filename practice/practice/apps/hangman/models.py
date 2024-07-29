from django.db import models

class Game(models.Model):
    word = models.CharField(max_length=200)
    guessed_letters = models.CharField(max_length=150, default='')
    max_attempts = models.IntegerField(default=6)
    attempts_left = models.IntegerField(default=6)

    def __str__(self):
        return self.word