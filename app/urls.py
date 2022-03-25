from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_equation', views.get_equation, name='get_equation')
]