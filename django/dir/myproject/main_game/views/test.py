from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def test(request):
    return HttpResponse('<a href="/main_game/">test</a>')

def test2(request):
    return render(request, 'test/base.html')