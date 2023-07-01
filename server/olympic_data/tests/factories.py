import factory

from olympic_data.models import (
    Country,
    City,
    Games,
    Sport,
    Discipline,
    Event,
    Athlete,
    MedalWin,
)


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
        django_get_or_create = ("country_code",)

    country_name = factory.Iterator(["France", "Italy", "Spain"])
    country_code = factory.Iterator(["FRA", "ITA", "ESP"])
    population = 70123824
    gdp_per_capita = 187634.0934235325532


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City
        django_get_or_create = ("city_name",)

    city_name = factory.Iterator(["Athens", "Beijing", "London"])


class GamesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Games

    year = factory.Iterator(["2004", "2008", "2012"])
    city = factory.SubFactory(CityFactory)


class SportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sport
        django_get_or_create = ("sport_name",)

    sport_name = factory.Iterator(["Aquatics", "Athletics", "Boxing"])


class DisciplineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Discipline
        django_get_or_create = (
            "discipline_name",
            "sport",
        )

    discipline_name = factory.Iterator(["Swimming", "Archery", "Badminton"])
    sport = factory.SubFactory(SportFactory)


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event
        django_get_or_create = (
            "event_name",
            "discipline",
        )

    event_name = factory.Iterator(["10m Springboard", "60Kg", "Shooting"])
    discipline = factory.SubFactory(DisciplineFactory)


class AthleteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Athlete
        django_get_or_create = ("athlete_name", "country", "gender")

    athlete_name = factory.Faker("name")
    country = factory.SubFactory(CountryFactory)
    gender = factory.Iterator([c[0] for c in Athlete.Gender.choices])


class MedalWinFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MedalWin

    athlete = factory.SubFactory(AthleteFactory)
    event = factory.SubFactory(EventFactory)
    games = factory.SubFactory(GamesFactory)
    medal_type = factory.Iterator([c[0] for c in MedalWin.Medals.choices])
