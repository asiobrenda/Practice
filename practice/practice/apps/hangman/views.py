from django.shortcuts import render, redirect
from .models import Game
import random

def select_random_word():
    word_list = Game.objects.all()  # Retrieve all words from the database
    return random.choice(word_list)

def home(request):
    game = None
    if request.method == 'POST':
        words = request.POST['word']
        game = Game.objects.create(word=select_random_word().word)

        return redirect('hangman:play', game.id)
    return render(request, 'hangman/index.html', {'game':game})


def play(request, game_id):
    game = Game.objects.get(id=game_id)
    feedback = ""

    if request.method == 'POST':
        letter = request.POST['letter'].lower()
        game.guessed_letters += letter
        if letter not in game.word.lower():
            game.attempts_left -= 1
            if game.attempts_left == 0:
                feedback = "You failed, the correct word was '{}'.".format(game.word)
        elif all(char.lower() in game.guessed_letters.lower() for char in game.word):
                feedback = "Congratulations you have won!"
    game.save()

    if 'play_again' in request.POST:
        # Create a new game object
        new_game = Game.objects.create(word=select_random_word().word)
        return redirect('hangman:play', game_id=new_game.id)


    return render(request,'hangman/play.html', {'game':game, 'feedback': feedback})