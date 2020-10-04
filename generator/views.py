from django.shortcuts import render
import string
import random
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'list': range(6, 16)})


def password(request):
    result = ''
    vals = [string.ascii_letters]
    length = int(request.GET.get("length", "12"))
    if request.GET.get("number"):
        vals.append(string.digits)
    if request.GET.get("uppercase"):
        vals.append(string.ascii_uppercase)
    if request.GET.get("special"):
        vals.append(string.punctuation)
    for i in range(length):
        idx = random.randint(0, len(vals) - 1)
        result += random.choice(vals[idx])
    return render(request, 'generator/password.html', {'password': result})


def about(request):
    return render(request, 'generator/about.html')
