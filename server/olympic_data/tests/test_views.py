import pytest
from django.urls import reverse
from olympic_data.tests.factories import AthleteFactory, CountryFactory, MedalWinFactory
from olympic_data.views import get_by_population


@pytest.mark.django_db
def test_medal_table_view(client):
    """
    Ensure that simple medal calculation is returned
    """
    YEAR = 2012
    url = reverse("medal-table", kwargs={"year": YEAR})
    country = CountryFactory()
    MedalWinFactory(country=country, medal_type="GOLD", games__year=YEAR)
    MedalWinFactory(country=country, medal_type="SILVER", games__year=YEAR)
    MedalWinFactory(country=country, medal_type="BRONZE", games__year=YEAR)

    res = client.get(url)

    assert len(res.data) == 1
    country_data = res.data[0]
    assert country_data["country_name"] == country.country_name
    assert country_data["country_code"] == country.country_code
    assert country_data["gold_medal_count"] == 1
    assert country_data["silver_medal_count"] == 1
    assert country_data["bronze_medal_count"] == 1


@pytest.mark.django_db
def test_medal_table_view_multiple_athletes_per_event(client):
    """
    Ensure medals are only counted once
    """
    YEAR = 2012
    url = reverse("medal-table", kwargs={"year": YEAR})
    country = CountryFactory()
    medal_win = MedalWinFactory(country=country, medal_type="GOLD", games__year=YEAR)
    athletes = AthleteFactory.create_batch(2, country=country)
    medal_win.athletes.add(*[athlete.pk for athlete in athletes])

    res = client.get(url)

    assert len(res.data) == 1
    country_data = res.data[0]
    assert country_data["country_name"] == country.country_name
    assert country_data["gold_medal_count"] == 1


@pytest.mark.django_db
def test_medal_table_view_year_filter(client):
    """
    Ensure the correct data is returned
    """
    YEAR = 2012
    url = reverse("medal-table", kwargs={"year": YEAR})
    country = CountryFactory()
    MedalWinFactory(country=country, medal_type="GOLD", games__year=YEAR)
    MedalWinFactory(country=country, medal_type="GOLD", games__year=YEAR)
    MedalWinFactory(country=country, medal_type="GOLD", games__year=YEAR + 1)
    MedalWinFactory(country=country, medal_type="SILVER", games__year=YEAR + 1)
    MedalWinFactory(country=country, medal_type="SILVER", games__year=YEAR)
    MedalWinFactory(country=country, medal_type="BRONZE", games__year=YEAR - 1)

    res = client.get(url)

    assert len(res.data) == 1
    country_data = res.data[0]
    assert country_data["country_name"] == country.country_name
    assert country_data["country_code"] == country.country_code
    assert country_data["gold_medal_count"] == 2
    assert country_data["silver_medal_count"] == 1
    assert country_data["bronze_medal_count"] == 0


@pytest.mark.django_db
def test_medal_table_view_incorrect_year(client):
    MedalWinFactory(medal_type="GOLD", games__year=2012)
    url = reverse("medal-table", kwargs={"year": 2013})

    res = client.get(url)

    assert res.status_code == 400


@pytest.mark.django_db
def test_medal_table_by_population(client):
    """
    Unit test for get_by_population
    """
    POPULATION = 100
    YEAR = 2004
    country = CountryFactory(population=POPULATION)
    MedalWinFactory(medal_type="GOLD", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="GOLD", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="SILVER", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="SILVER", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="SILVER", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="SILVER", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="SILVER", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="BRONZE", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="BRONZE", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="BRONZE", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="BRONZE", country=country, games__year=YEAR)

    data = get_by_population(YEAR)

    # Expect 50 people per Gold medal
    assert data[0].population_per_gold_medal == 50
    assert data[0].population_per_silver_medal == 20
    assert data[0].population_per_bronze_medal == 25


@pytest.mark.skip
@pytest.mark.django_db
def test_medal_table_by_population_zero():
    """
    When a country has won zero medals, Django can't handle divsion by zero
    """
    CountryFactory()

    data = get_by_population(2004)

    assert data == []


@pytest.mark.django_db
def test_medal_table_view__population(client):
    """
    Ensure that simple medal population is returned
    """
    YEAR = 2012
    POPULATION = 100

    url = reverse("medal-table", kwargs={"year": YEAR})
    country = CountryFactory(population=POPULATION)
    MedalWinFactory(medal_type="GOLD", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="GOLD", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="SILVER", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="SILVER", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="SILVER", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="SILVER", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="SILVER", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="BRONZE", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="BRONZE", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="BRONZE", country=country, games__year=YEAR)
    MedalWinFactory(medal_type="BRONZE", country=country, games__year=YEAR)

    res = client.get(url)

    assert len(res.data) == 1
    country_data = res.data[0]
    assert country_data["country_name"] == country.country_name
    assert country_data["country_code"] == country.country_code
    assert country_data["gold_medal_count"] == 2
    assert country_data["silver_medal_count"] == 5
    assert country_data["bronze_medal_count"] == 4
    assert country_data["population_per_gold_medal"] == 50
    assert country_data["population_per_silver_medal"] == 20
    assert country_data["population_per_bronze_medal"] == 25
