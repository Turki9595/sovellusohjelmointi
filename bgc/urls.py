# Definec URL patterns for cbc
from django.urls import path
from . import views

app_name = 'bgc'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page with all the games
    path('b_games/', views.b_games, name='b_games'),
    #Detail page for a single game
    path('b_games/<int:b_game_id>/', views.b_game, name='b_game'),
    #page for adding a new board game
    path('new_b_game/', views.new_b_game, name = 'new_b_game'),
    #page for adding new review
    path('new_review/<int:b_game_id>/',views.new_review, name='new_review'),
    #page for editing an review
    path('edit_review/<int:review_id>/', views.edit_review, name ='edit_review'),
]