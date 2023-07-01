from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=50, null=False, blank=False)
    country_code = models.SlugField(max_length=3, null=False, blank=False)
    population = models.IntegerField(null=True, blank=True)
    gdp_per_capita = models.DecimalField(
        null=True, blank=True, decimal_places=30, max_digits=50
    )

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.city_name


class Games(models.Model):
    year = models.PositiveSmallIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}-{self.year}"


class Sport(models.Model):
    sport_name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.sport_name


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=200, null=False, blank=False)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sport}-{self.discipline_name}"


class Athlete(models.Model):
    class Gender(models.TextChoices):
        MEN = "MEN"
        WOMEN = "WOMEN"

    athlete_name = models.CharField(max_length=200, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    gender = models.CharField(choices=Gender.choices)

    def __str__(self):
        return f"{self.athlete_name}-{self.country}"


class Event(models.Model):
    """
    An event, combination of discipline/sport and event name with a gender.

    N.B. Not all events are single gender. There is no simple way to infer which
    are not from the dataset.
    """

    event_name = models.CharField(max_length=200, null=False, blank=False)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    gender = models.CharField(choices=Athlete.Gender.choices)

    def __str__(self):
        return f"{self.discipline}-{self.event_name}"


class MedalWin(models.Model):
    class Medals(models.TextChoices):
        GOLD = "GOLD"
        SILVER = "SILVER"
        BRONZE = "BRONZE"

    athletes = models.ManyToManyField(Athlete)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    medal_type = models.CharField(choices=Medals.choices)

    def __str__(self):
        return f"{self.games}-{self.event}-{self.country}"
