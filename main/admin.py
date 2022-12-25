from django.contrib import admin
from .models import Carousel, Management, Player, Creator, Event
# Register your models here.
admin.site.register(Carousel)
admin.site.register(Management)
admin.site.register(Player)
admin.site.register(Creator)
admin.site.register(Event)