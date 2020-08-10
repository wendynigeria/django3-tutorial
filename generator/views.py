from django.shortcuts import render
import random

# Create your views here.
def home(request):    
    return render(request, 'generator/home.html', {})

def password(request):

    password = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length'))

    if request.GET.get('upper'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*_-+'))


    for x in range(length):
        password += random.choice(characters)
    context = {'password': password}

    return render(request, 'generator/password.html', context)
