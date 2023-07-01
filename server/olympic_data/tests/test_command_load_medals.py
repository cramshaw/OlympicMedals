import pytest
from django.core.management import call_command
from olympic_data.management.commands.load_medals import process_medal_row
from olympic_data.tests.factories import (
    CountryFactory,
    GamesFactory,
    EventFactory,
    DisciplineFactory,
    AthleteFactory,
    SportFactory,
    MedalWinFactory,
)
from django.core.management.base import CommandError
from olympic_data.models import (
    City,
    Country,
    Games,
    Sport,
    Discipline,
    Event,
    Athlete,
    MedalWin,
)

SINGLE_MEDAL_CSV = "olympic_data/tests/test_data/test_medal.csv"


@pytest.fixture
def example_row():
    COUNTRY_CODE = "CHN"
    CountryFactory(country_code=COUNTRY_CODE)
    return {
        "Year": 2004,
        "City": "Athens",
        "Sport": "Aquatics",
        "Discipline": "Diving",
        "Athlete": "HU, Jia",
        "Country": COUNTRY_CODE,
        "Gender": "Men",
        "Event": "10M Platform",
        "Medal": "Gold",
    }


@pytest.mark.parametrize(
    "field",
    [
        "Year",
        "City",
        "Sport",
        "Discipline",
        "Athlete",
        "Gender",
        "Event",
        "Medal",
    ],
)
@pytest.mark.django_db
def test_load_medal_missing_field_throws(example_row, field):
    """
    Test that a file won't be processed if a required field is missing
    """
    del example_row[field]

    with pytest.raises(CommandError) as e:
        process_medal_row(example_row)
        assert e.value.args[0] == f"Row missing {field}"


@pytest.mark.django_db
def test_process_medal_row_nothing_exists(example_row):
    """
    Happy path test
    """
    CountryFactory(country_code="CHN")
    assert City.objects.count() == 0
    assert Games.objects.count() == 0
    assert Sport.objects.count() == 0
    assert Discipline.objects.count() == 0
    assert Event.objects.count() == 0
    assert Athlete.objects.count() == 0
    assert MedalWin.objects.count() == 0

    process_medal_row(example_row)

    assert City.objects.count() == 1
    assert Games.objects.count() == 1
    assert Sport.objects.count() == 1
    assert Discipline.objects.count() == 1
    assert Event.objects.count() == 1
    assert Athlete.objects.count() == 1
    assert MedalWin.objects.count() == 1


@pytest.mark.django_db
def test_process_medal_row_games_exist(example_row):
    games = GamesFactory()
    assert Games.objects.count() == 1
    assert MedalWin.objects.count() == 0
    example_row["Year"] = games.year
    example_row["City"] = games.city.city_name

    process_medal_row(example_row)

    assert Games.objects.count() == 1
    assert MedalWin.objects.count() == 1


@pytest.mark.django_db
def test_process_medal_row_sport_exists(example_row):
    sport = SportFactory()
    assert Sport.objects.count() == 1
    assert MedalWin.objects.count() == 0
    example_row["Sport"] = sport.sport_name

    process_medal_row(example_row)

    assert Sport.objects.count() == 1
    assert MedalWin.objects.count() == 1


@pytest.mark.django_db
def test_process_medal_row_discipline_exists(example_row):
    discipline = DisciplineFactory()
    assert Discipline.objects.count() == 1
    assert MedalWin.objects.count() == 0
    example_row["Discipline"] = discipline.discipline_name
    example_row["Sport"] = discipline.sport.sport_name

    process_medal_row(example_row)

    assert Discipline.objects.count() == 1
    assert MedalWin.objects.count() == 1


@pytest.mark.django_db
def test_process_medal_row_event_exists(example_row):
    event = EventFactory()
    assert Event.objects.count() == 1
    assert MedalWin.objects.count() == 0
    example_row["Event"] = event.event_name
    example_row["Discipline"] = event.discipline.discipline_name
    example_row["Sport"] = event.discipline.sport.sport_name

    process_medal_row(example_row)

    assert Event.objects.count() == 1
    assert MedalWin.objects.count() == 1


@pytest.mark.django_db
def test_process_medal_row_athlete_exists(example_row):
    athlete = AthleteFactory()
    assert Athlete.objects.count() == 1
    assert MedalWin.objects.count() == 0
    example_row["Athlete"] = athlete.athlete_name
    example_row["Country"] = athlete.country.country_code
    example_row["Gender"] = athlete.gender[1]

    process_medal_row(example_row)

    assert Event.objects.count() == 1
    assert MedalWin.objects.count() == 1


@pytest.mark.django_db
def test_process_medal_row_medal_exists(example_row):
    medal_win = MedalWinFactory()
    assert MedalWin.objects.count() == 1
    example_row["Year"] = medal_win.games.year
    example_row["City"] = medal_win.games.city.city_name
    example_row["Sport"] = medal_win.event.discipline.sport.sport_name
    example_row["Discipline"] = medal_win.event.discipline.discipline_name
    example_row["Athlete"] = medal_win.athlete.athlete_name
    example_row["Country"] = medal_win.athlete.country.country_code
    example_row["Gender"] = medal_win.athlete.gender.capitalize()
    example_row["Event"] = medal_win.event.event_name
    example_row["Medal"] = medal_win.medal_type.capitalize()

    process_medal_row(example_row)

    assert MedalWin.objects.count() == 1


@pytest.mark.django_db
def test_process_medal_row_pending(example_row):
    """
    Not all rows have an athlete, handle by skipping
    """
    assert MedalWin.objects.count() == 0
    example_row["Athlete"] = "Pending"

    process_medal_row(example_row)

    assert MedalWin.objects.count() == 0


@pytest.mark.django_db
def test_process_medal_row_missing_country(example_row):
    """
    Test that we skip without breaking as some rows are missing countries
    """
    assert MedalWin.objects.count() == 0
    example_row["Country"] = "badcountrycode"

    process_medal_row(example_row)

    assert MedalWin.objects.count() == 0


@pytest.mark.django_db
def test_load_medals_no_path():
    with pytest.raises(CommandError) as e:
        call_command("load_medals")
        assert (
            e.value.args[0]
            == "Error: the following arguments are required: --file_path"
        )


@pytest.mark.django_db
def test_load_medals_invalid_path():
    with pytest.raises(CommandError) as e:
        call_command("load_medals", file_path="/nothing/nowhere/ever")
        assert (
            e.value.args[0] == "The path /nothing/nowhere/ever does not contain a file."
        )


@pytest.mark.django_db
def test_load_medals_medals_loaded():
    """
    Happy path e2e test
    """
    CountryFactory(country_code="CHN")
    assert MedalWin.objects.count() == 0
    call_command("load_medals", file_path=SINGLE_MEDAL_CSV)
    assert MedalWin.objects.count() == 1
