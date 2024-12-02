from django.urls import path
from . import views

urlpatterns = [
    path("", views.leaderboard, name="home"),  # Add this line for the default path
    path("add_player/", views.add_player, name="add_player"),
    path("leaderboard/", views.leaderboard, name="leaderboard"), 
]
