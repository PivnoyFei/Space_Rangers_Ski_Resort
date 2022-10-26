from django.urls import path

from games import views

app_name = 'games'


urlpatterns = [
    path('', views.index, name='index'),
    path('game', views.game, name='game'),
]
