from django.shortcuts import render


def c1(request):
    return render(request, 'c1.html')


def c2(request):
    return render(request, 'c2.html')


def c3(request):
    return render(request, 'c3.html')
