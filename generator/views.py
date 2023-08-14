from random import randint, choice
from string import ascii_letters, digits, punctuation

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'generator/index.html')


def easy_password(request):
    difficulty = request.GET.get('difficulty', 'easy')
    route = request.path
    all_chars = list(ascii_letters)

    password_length = randint(8, 20)
    password = ''.join([choice(all_chars) for _ in range(password_length)])

    return render(request, 'generator/password.html', context={'generate': password,'route':route,'difficulty': difficulty})


def medium_password(request):
    difficulty = request.GET.get('difficulty', 'medium')
    route = request.path
    all_chars = list(ascii_letters + digits)

    password_length = randint(8, 20)
    password = ''.join([choice(all_chars) for _ in range(password_length)])

    return render(request, 'generator/password.html', context={'generate': password,'route':route,'difficulty': difficulty})

def hard_password(request):
    difficulty = request.GET.get('difficulty', 'hard')
    route = request.path
    all_chars = list(ascii_letters + digits + punctuation)

    password_length = randint(8, 20)
    password = ''.join([choice(all_chars) for _ in range(password_length)])

    return render(request, 'generator/password.html', context={'generate': password,'route':route,'difficulty': difficulty})