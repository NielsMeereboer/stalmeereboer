from django.shortcuts import render


def home(request):
    return render(request, 'stalmeereboer/home.html')


def about(request):
    return render(request, 'stalmeereboer/about.html')


def ponies(request):
    return render(request, 'stalmeereboer/ponies.html')


def news(request):
    return render(request, 'stalmeereboer/news.html')


def contact(request):
    return render(request, 'stalmeereboer/contact.html')