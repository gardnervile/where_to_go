from django.http import HttpResponse
from django.shortcuts import render

def show_places(request):
    return render(request, 'page.html')
