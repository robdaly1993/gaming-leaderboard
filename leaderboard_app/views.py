from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Player
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_player(request):
    if request.method == "POST":
        player_name = request.POST.get("name")
        if not player_name:
            return JsonResponse({"error": "Name is required"}, status=400)
        
        player = Player.objects.create(name=player_name)
        return JsonResponse({"id": player.id, "name": player.name, "total_score": player.total_score})
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=405)


def home(request):
    return HttpResponse("<h1>Welcome to the Gaming Leaderboard! zdfzdfsdfsdf</h1>")


def leaderboard(request):
    # Query the players from the database, sorted by total_score descending
    players = Player.objects.all().order_by('-total_score')
    
    # Pass players to the template
    return render(request, 'leaderboard.html', {"players": players})
