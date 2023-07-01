from django.urls import reverse
import pytest

from olympic_data.tests.factories import CountryFactory, MedalWinFactory
from olympic_data.tests.factories import AthleteFactory


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
