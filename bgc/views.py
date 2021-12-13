from django.shortcuts import render
from .models import B_game,Review
# Create your views here.
def index(request):
    #homepage
    return render(request, 'bgc/index.html')

def b_games(request):
    #show all boardgames
    b_games = B_game.objects.order_by('date_added')
    context = {'b_games': b_games}
    return render(request, 'bgc/b_games.html', context)

def b_game(request, b_game_id):
    #show single game and all its reviews
    b_game = B_game.objects.get(id=b_game_id)
    reviews = b_game.review_set.order_by('-date_added')
    context = {'b_game': b_game, 'reviews':  reviews}
    return render(request, 'bgc/b_game.html', context)
