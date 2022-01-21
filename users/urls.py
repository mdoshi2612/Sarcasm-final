from django.urls import path
from .import views
from .views import Play

urlpatterns=[
	path('',views.home, name='home'),
	path('faq',views.faq, name='faq'),
	path('play',Play.as_view(), name='play'),
	path('generatepassword',views.generatepassword, name='generatepassword'),
	path('login', views.login1, name='login'),
	path('leaderboard',views.leaderboard, name='leaderboard'),
	path('bonus',views.Bonus.as_view(),name='bonus'),
	path('team',views.ourteam,name='ourteam'),
	path('success', views.success, name="success"),
	path('/increase_bonus_level', views.increase_bonus_level, name="increase_bonus_level"),
	path('skip', views.increase_bonus_level, name="increase_bonus_level"),
	path('csv_teams',views.csv_teams,name='csv_teams'),
	path('image', views.image, name='image'),	
	path('navbar', views.navbar, name='navbar'),
]
