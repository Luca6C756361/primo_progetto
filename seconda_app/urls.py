from django.urls import path
from seconda_app.views import index,es_if,else_if_elif,es_for
app_name="seconda_app"
urlpatterns=[
    path('index',index,name='index'),
    path('es_if',es_if,name='es_if'),
    path('else_if_elif',else_if_elif,name='else_if_elif'),
    path('es_for',es_for,name='es_for'),
]