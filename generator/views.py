from random import randint, choice
from string import ascii_letters, digits, punctuation

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'generator/index.html')


def easy_password(request):
    all = []
    res = ''
    for i in ascii_letters:
        all.append(i)

    num = randint(8, 20)
    print(num)
    while num:
        num -= 1
        x = choice(all)
        res += x
    return render(request, 'generator/password.html',context={'generate': res})


def medium_password(request):
    all = []
    res = ''

    for i in digits:
        all.append(i)

    for i in ascii_letters:
        all.append(i)

    num = randint(8, 20)
    while num:
        num -= 1
        x = choice(all)
        res += x
    return render(request, 'generator/password.html',context={'generate': res})

def hard_password(request):
    all = []
    res = ''

    for i in digits:
        all.append(i)

    for i in ascii_letters:
        all.append(i)

    for i in punctuation:
        all.append(i)

    num = randint(8, 20)
    while num:
        num -= 1
        x = choice(all)
        res += x
    return render(request, 'generator/password.html',context={'generate': res})