from django.shortcuts import render

from django.http import JsonResponse
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
