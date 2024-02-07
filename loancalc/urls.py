from django.urls import path
from . import views


urlpatterns = [
    path('',views.loancalc,name='loancalc')    
]
