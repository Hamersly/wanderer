from django.shortcuts import render
from .models import *


def index(request):
    tl = TL.objects.all()
    context = {'tl': tl}
    return render(request, 'app/index.html', context)


