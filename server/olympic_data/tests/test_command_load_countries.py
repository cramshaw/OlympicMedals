import pytest
from django.core.management import call_command
from olympic_data.management.commands.load_countries import process_country_row
from olympic_data.models import Country
from olympic_data.tests.factories import CountryFactory
from django.core.management.base import CommandError

SINGLE_COUNTRY_CSV = "olympic_data/tests/test_data/test_country.csv"


@pytest.mark.django_db
def test_load_countries_no_path():
    with pytest.raises(CommandError) as e:
        call_command("load_countries")
        assert (
            e.value.args[0]
            == "Error: the following arguments are required: --file_path"
        )


@pytest.mark.django_db
def test_load_countries_invalid_path():
    with pytest.raises(CommandError) as e:
        call_command("load_countries", file_path="/nothing/nowhere/ever")
        assert (
            e.value.args[0] == "The path /nothing/nowhere/ever does not contain a file."
        )


@pytest.mark.django_db
def test_load_countries_country_loaded():
    """
    Happy path test
    """
    assert Country.objects.count() == 0
    call_command("load_countries", file_path=SINGLE_COUNTRY_CSV)
    assert Country.objects.count() == 1


@pytest.mark.django_db
def test_process_country_row_country_missing():
    row = {
        "Code": "ARG",
        "Population": "43416755",
        "GDP per Capita": "13431.8783398577",
    }
    with pytest.raises(CommandError) as e:
        process_country_row(row)
        assert e.value.args[0] == "Row missing Country"


@pytest.mark.django_db
def test_process_country_row_code_missing():
    row = {
        "Country": "Argentina",
        "Population": "43416755",
        "GDP per Capita": "13431.8783398577",
    }
    with pytest.raises(CommandError) as e:
        process_country_row(row)
        assert e.value.args[0] == "Row missing Code"


@pytest.mark.django_db
def test_process_country_row_population_gdp_updated():
    row = {
        "Country": "Argentina",
        "Code": "ARG",
        "Population": "43416755",
        "GDP per Capita": "13431.8783398577",
    }
    CountryFactory(country_name=row["Country"], country_code=row["Code"], population=0)
    country, created = process_country_row(row)
    assert created is False
    assert country.population == row["Population"]
    assert country.gdp_per_capita == row["GDP per Capita"]


@pytest.mark.django_db
def test_process_country_row_created():
    """
    Happy path test
    """
    row = {
        "Country": "Argentina",
        "Code": "ARG",
        "Population": "43416755",
        "GDP per Capita": "13431.8783398577",
    }
    country, created = process_country_row(row)
    assert created is True
    assert country.country_name == row["Country"]
    assert country.country_code == row["Code"]
    assert country.population == row["Population"]
    assert country.gdp_per_capita == row["GDP per Capita"]


@pytest.mark.django_db
def test_process_country_row_created_missing_data():
    """
    Happy path test
    """
    row = {
        "Country": "Argentina",
        "Code": "ARG",
        "Population": "",
        "GDP per Capita": "",
    }
    country, created = process_country_row(row)
    assert created is True
    assert country.country_name == row["Country"]
    assert country.country_code == row["Code"]
    assert country.population is None
    assert country.gdp_per_capita is None


@pytest.mark.django_db
def test_process_country_asterisk_stripped():
    """
    Happy path test
    """
    row = {
        "Country": "Argentina*",
        "Code": "ARG",
        "Population": "",
        "GDP per Capita": "",
    }
    country, created = process_country_row(row)
    assert country.country_name == "Argentina"
