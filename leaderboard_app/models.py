from django.db import models

from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class GameScore(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.name}: {self.score}"