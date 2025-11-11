from django.shortcuts import render
from .models import Game, Genre
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def home(request):
    games = Game.objects.all()[:3]
    return render(request, 'game_pages/home.html', {'games': games})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'game_pages/genres.html', {'genres': genres})

def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    games = Game.objects.filter(genre=genre)
    return render(request, 'game_pages/genre_detail.html', {'genre': genre, 'games': games})


def games_list(request):
    games = Game.objects.all()
    return render(request, 'game_pages/games_list.html', {'games': games})

def favorites_list(request):
    favorite_ids = request.session.get('favorite_games', [])
    favorites = Game.objects.filter(id__in=favorite_ids)
    return render(request, 'game_pages/favorites.html', {'favorites': favorites})
    
def add_to_favorite(request, game_id):
    favorites = request.session.get('favorite_games', [])

    if game_id not in favorites:
        favorites.append(game_id)
        request.session['favorite_games'] = favorites
        game = get_object_or_404(Game, id=game_id)
        messages.success(request, f'🎉 {game.title} was just added to your favorites!')
    else:
        game = get_object_or_404(Game, id=game_id)
        messages.warning(request, f'⚠ {game.title} is already in your favorites.')

    return redirect('games_list')

def remove_from_favorite(request, game_id):
    favorites = request.session.get('favorite_games', [])
    if game_id in favorites:
        favorites.remove(game_id)
        request.session['favorite_games'] = favorites
        messages.success(request, 'Game removed from favorites.')
    else:
        messages.warning(request, 'Game is not in favorites.')
    return redirect('favorites_list')