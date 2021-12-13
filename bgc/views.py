from django.shortcuts import render, redirect

from bgc.forms import B_gameForm,ReviewForm
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

def new_b_game(request):
    #add a new b_game
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = B_gameForm()
    else:
        # POST data submitted; process data.
        form = B_gameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bgc:b_games')
    #Display a blank or invalid form.
    context = {'form':form}
    return render(request, 'bgc/new_b_game.html',context)


def new_review(request, b_game_id):
    #add a new review for a particular b_game

    b_game = B_game.objects.get(id=b_game_id)

    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = ReviewForm()
    else:
        # POST data submitted; process data.
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.b_game = b_game
            new_review.save()
            return redirect('bgc:b_game', b_game_id = b_game_id)
    #Display a blank or invalid form.
    context = {'b_game': b_game, 'form': form}
    return render(request, 'bgc/new_review.html',context)

def edit_review(request, review_id):
    #Edit an existing review.
    review = Review.objects.get(id=review_id)
    b_game = review.b_game
    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry.
        form = ReviewForm(instance = review)
    else:
        #POST data submitted ; process data.
        form = ReviewForm(instance = review, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('bgc:b_game', b_game_id = b_game.id)
    context = {'review': review, 'b_game': b_game, 'form':form}
    return render(request, 'bgc/edit_review.html', context)