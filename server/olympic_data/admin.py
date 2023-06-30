from django.contrib import admin
from olympic_data.models import (
    Athlete,
    City,
    Country,
    Discipline,
    Event,
    Games,
    MedalWin,
)


# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ...


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    ...


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    ...


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    ...


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ...


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    ...


@admin.register(MedalWin)
class MedalWinAdmin(admin.ModelAdmin):
    ...
