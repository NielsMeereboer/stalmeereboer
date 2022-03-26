from django.shortcuts import render


def home(request):
    return render(request, 'stalmeereboer/home.html')


def hengsten(request):
    return render(request, 'stalmeereboer/hengsten.html')
