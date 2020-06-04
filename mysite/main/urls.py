from django.urls import path
from .views import(
    GameListView,
    GameDetailView,
    GameCreateView,
    GameUpdateView,
    GameDeleteView
)
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("home/", views.home, name='home'),
    path("find/", views.find, name='find'),
    path("play/", views.play, name='play'),
    path("about/", views.about, name='about'),
    path("scoreboard/", views.scoreboard, name='scoreboard'),
    path("user_games/", GameListView.as_view(), name='user_games'),
    path("games/<int:pk>/", GameDetailView.as_view(), name='game-detail'),
    path("games/new/", GameCreateView.as_view(), name='game-create'),
    path("games/<int:pk>/update/", GameUpdateView.as_view(), name='game-update'),
    path("games/<int:pk>/delete/", GameDeleteView.as_view(), name='game-delete'),
    path("jogo1/", views.jogo1, name='jogo1'),
    path("jogo2/", views.jogo2, name='jogo2'),
    path("jogo3/", views.jogo3, name='jogo3'),


]
