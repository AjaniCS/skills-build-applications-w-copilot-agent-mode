from django.db import models
from django.contrib.auth import get_user_model

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.name

class Activity(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.name} - {self.user}"

class Leaderboard(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	score = models.IntegerField()
	def __str__(self):
		return f"{self.user} - {self.score}"

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.name} - {self.user}"
