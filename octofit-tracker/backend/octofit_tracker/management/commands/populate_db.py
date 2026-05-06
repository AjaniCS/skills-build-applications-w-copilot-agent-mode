from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass')
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass')

        # Activities
        Activity.objects.create(name='Run', user='ironman', team='Marvel')
        Activity.objects.create(name='Swim', user='batman', team='DC')
        Activity.objects.create(name='Bike', user='superman', team='DC')
        Activity.objects.create(name='Yoga', user='captain', team='Marvel')

        # Leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', score=100)
        Leaderboard.objects.create(user='batman', team='DC', score=90)
        Leaderboard.objects.create(user='superman', team='DC', score=95)
        Leaderboard.objects.create(user='captain', team='Marvel', score=98)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups', user='ironman')
        Workout.objects.create(name='Situps', description='Do 100 situps', user='batman')
        Workout.objects.create(name='Squats', description='Do 75 squats', user='superman')
        Workout.objects.create(name='Plank', description='Hold plank for 2 min', user='captain')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
