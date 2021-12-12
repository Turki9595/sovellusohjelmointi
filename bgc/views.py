from django.shortcuts import render
from .models import B_game
# Create your views here.
def index(request):
    #homepage
    return render(request, 'bgc/index.html')

def b_games(request):
    #show all boardgames
    b_games = B_game.objects.order_by('date_added')
    context = {'b_games': b_games}
    return render(request, 'bgc/b_games.html', context)