from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def index(request):
    # return HttpResponse('<h1>Hello Django!</h1>')
    return render(request, 'index.html', {'password': '123456'})


def password(request):
    characters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    if request.GET.get('uppercase'):
        characters += [chr(i) for i in range(ord('A'), ord('Z')+1)]
    if request.GET.get('number'):
        characters += [str(i) for i in range(0, 10)]
    if request.GET.get('special'):
        characters += list('!@#$%^&*')
    # print(characters)
    length = request.GET.get(
        'input-length') if request.GET.get('input-length') else request.GET.get('length')
    password = ''.join([random.choice(characters)
                        for i in range(eval(length))])
    print(request.GET)
    return render(request, 'password.html', {'password': password})
