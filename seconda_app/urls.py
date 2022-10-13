from django.urls import path
from seconda_app.views import es_if,else_if_elif
app_name="seconda_app"
urlpatterns=[
    path('es_if',es_if,name='es_if'),
    path('else_if_elif',else_if_elif,name='else_if_elif'),




]