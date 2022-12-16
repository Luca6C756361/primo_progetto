from django.urls import path
from  prova_pratica_2.views import view_a,view_b,view_c,index_prova_2
app_name="prova_pratica_2"
urlpatterns=[
    path('view_a',view_a,name='view_a'),
    path('view_b',view_b,name='view_b'),
    path('view_c',view_c,name='view_c'),
    path('index_prova_2',index_prova_2,name='index_prova_2'),
]