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

    def save(self, *args, **kwargs):
        # Call the original save method
        super().save(*args, **kwargs)
        # Update the player's total score
        self.player.total_score += self.score
        self.player.save()

class Match(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='matches')
    match_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"Match for {self.player.name} on {self.match_date.strftime('%Y-%m-%d')} with score {self.score}"