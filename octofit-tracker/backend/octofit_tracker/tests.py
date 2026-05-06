from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

class APITest(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com', password='pass')
		self.team = Team.objects.create(name='Test Team')
		self.activity = Activity.objects.create(name='Test Activity', user=self.user, team=self.team)
		self.leaderboard = Leaderboard.objects.create(user=self.user, team=self.team, score=10)
		self.workout = Workout.objects.create(name='Test Workout', description='desc', user=self.user)

	def test_api_root(self):
		response = self.client.get(reverse('api-root'))
		self.assertEqual(response.status_code, 200)

	def test_users_endpoint(self):
		response = self.client.get('/users/')
		self.assertEqual(response.status_code, 200)

	def test_teams_endpoint(self):
		response = self.client.get('/teams/')
		self.assertEqual(response.status_code, 200)

	def test_activities_endpoint(self):
		response = self.client.get('/activities/')
		self.assertEqual(response.status_code, 200)

	def test_leaderboard_endpoint(self):
		response = self.client.get('/leaderboard/')
		self.assertEqual(response.status_code, 200)

	def test_workouts_endpoint(self):
		response = self.client.get('/workouts/')
		self.assertEqual(response.status_code, 200)
