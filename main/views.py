from datetime import date

from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Carousel, Management, Player, Creator, Event

# Create your views here.
def index(request):
    carousel_obj = Carousel.objects.all()
    management_obj = Management.objects.all()
    events_obj = Event.objects.filter(date__gte=date.today())
    
    obj = {
        'carousel': carousel_obj,
        'management': management_obj,
        'event': events_obj
    }
    return render(request, 'index.html', obj)

def roster(request):
    players_obj = Player.objects.all()
    obj = {
        'players': players_obj
    }
    return render(request, 'roster.html', obj)

def creators(request):
    creator_obj = Creator.objects.all()
    obj = {
        'creators': creator_obj
    }
    return render(request, 'creators.html', obj)

def manager(request, id):
    manager_obj = Management.objects.get(id=id)
    temp = model_to_dict(manager_obj)
    
    obj = {
        'player':temp,
        
    }
    return render(request, 'manager.html', obj)

def player(request, id):
    player_obj = Player.objects.get(id=id)
    temp = model_to_dict(player_obj)
    print(temp)

    vids = temp['streams']
    streams = []

    if vids and vids != '#':    
        for x in vids.split(','):
            y = x.strip("\r\n")        
            streams.append(y)
    
    obj = {
        'player':temp,
        'streams':streams
    }
    return render(request, 'player.html', obj)

def creator(request, id):
    creator_obj = Creator.objects.get(id=id)
    temp = model_to_dict(creator_obj)
    
    vids = temp['streams']
    streams = []

    if vids and vids != '#':    
        for x in vids.split(','):
            y = x.strip("\r\n")        
            streams.append(y)
    
    obj = {
        'player':temp,
        'streams':streams
    }
    return render(request, 'player.html', obj)


def about(request):
    return render(request, 'about.html', {})

def events(request):
    events_obj_upcoming = Event.objects.filter(date__gte=date.today())
    events_obj_past = Event.objects.filter(date__lt=date.today())
    obj = {
        'upcoming':events_obj_upcoming,
        'past':events_obj_past,
    }
    return render(request, 'events.html', obj)


def not_found_view(request, exception):
    return render(request, '404.html', status=404)