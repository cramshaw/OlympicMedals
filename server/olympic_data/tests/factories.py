import factory

from olympic_data.models import Country


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
        django_get_or_create = ("country_code",)

    country_name = factory.Iterator(["France", "Italy", "Spain"])
    country_code = factory.Iterator(["FRA", "ITA", "ESP"])
    population = 70123824
    gdp_per_capita = 187634.0934235325532
