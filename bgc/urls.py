# Definec URL patterns for cbc
from django.urls import path
from . import views

app_name = 'bgc'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page with all the games
    path('b_games/', views.b_games, name='b_games')
]