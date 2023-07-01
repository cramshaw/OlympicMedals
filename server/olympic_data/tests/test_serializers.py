import pytest
from olympic_data.serializers import CountryMedalSerializer
from olympic_data.tests.factories import CountryFactory
from olympic_data.tests.factories import MedalWinFactory
from olympic_data.views import MedalTableView


@pytest.mark.django_db
def test_country_medal_serializer():
    YEAR = 2012
    country = CountryFactory()

    MedalWinFactory.create_batch(
        1, country=country, medal_type="GOLD", games__year=YEAR
    )
    MedalWinFactory.create_batch(
        2, country=country, medal_type="SILVER", games__year=YEAR
    )
    MedalWinFactory.create_batch(
        1, country=country, medal_type="BRONZE", games__year=YEAR
    )

    CountryMedalSerializer

    MTB = MedalTableView()
    MTB.kwargs = {"year": YEAR}
    # Use the real queryset method so if that changes, we know the serializer is broken
    qs = MTB.get_queryset()
    serializer = CountryMedalSerializer(qs, many=True)

    assert serializer.data[0]["country_name"] == country.country_name
    assert serializer.data[0]["country_code"] == country.country_code
    assert serializer.data[0]["gold_medal_count"] == 1
    assert serializer.data[0]["silver_medal_count"] == 2
    assert serializer.data[0]["bronze_medal_count"] == 1
