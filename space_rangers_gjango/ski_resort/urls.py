from django.urls import path

from ski_resort import views

app_name = 'ski_resort'

urlpatterns = [
    path('ski_start/', views.ski_start, name='ski_start'),
    path('ski_continue/', views.ski_continue, name='ski_continue'),
    path('ask/', views.ask, name='ask'),
    path('building/', views.building, name='building'),
]
