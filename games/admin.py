from django.contrib import admin

# Register your models here.
from .models import Genre, Game

admin.site.register(Genre)
admin.site.register(Game)
