from django.urls import path
from prova_pratica_0.views import index,somma,media

app_name="prova_pratica_0"
urlpatterns=[
    path('somma',somma,name='somma'),
    path('media',media,name='media'),
    path('index',index,name='index'),
]
