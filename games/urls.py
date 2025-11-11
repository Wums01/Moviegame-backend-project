from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/<int:genre_id>/', views.genre_detail, name='genre_detail'),
    path('games/', views.games_list, name='games_list'),
    path('favorites/', views.favorites_list, name='favorites_list'),
    path('add_to_favorite/add/<int:game_id>/', views.add_to_favorite, name='add_to_favorite'),
    path('favorites/remove/<int:game_id>/', views.remove_from_favorite, name='remove_from_favorite'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
