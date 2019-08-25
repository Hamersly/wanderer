from django.shortcuts import render
from .models import *


def index(request):
    tl = TL.objects.all()
    context = {'tl': tl}
    return render(request, 'app/index.html', context)

def routes(request):
    return render(request, 'app/routes.html')

def outfit(request):
    return render(request, 'app/outfit.html')
