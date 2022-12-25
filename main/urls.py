from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('roster', views.roster, name='roster'),
    path('creators', views.creators, name='creators'),
    path('creators/<int:id>', views.creator, name='creator'),
    path('player/<int:id>', views.player, name='player'),
    path('manager/<int:id>', views.manager, name='manager'),
    path('events', views.events, name='events'),
    path('about', views.about, name='about')
] 

handler404 = 'main.views.not_found_view'