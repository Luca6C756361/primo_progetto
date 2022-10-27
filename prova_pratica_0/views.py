from importlib.resources import contents
from multiprocessing import context
from re import S, X
from django.shortcuts import render
import random


# Create your views here.
def somma(request):
    x=random.randint(1,10)
    y=random.randint(1,10)
    context={ 
        'var1':x,
        'var2':y,
        'somma': x+y,
    }
    return render(request,"somma.html",context)
def media(request):
    lista=[]
    s=0
    for i in range(30):
        num=random.randint(0,10)
        s+=num
        lista.append(num)
        media=s/30
        context={
            'lista':lista,
            'media':media
        }
    return render(request,"media.html",context)
def index_prova(request):
    return render(request,"index_prova.html")

