import logging
from csv import DictReader
from os.path import isfile

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
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
from .helpers import check_required_present

logger = logging.getLogger(__name__)


def process_medal_row(row: dict):
    """
    Method to check required fields are included and create/update

    :param row: Row of CSV file
    """
    for key in [
        "Year",
        "City",
        "Sport",
        "Discipline",
        "Athlete",
        "Country",
        "Gender",
        "Event",
        "Medal",
    ]:
        check_required_present(row, key)

    # Get or create city
    city, created = City.objects.get_or_create(city_name=row["City"])
    # Get or Create Games
    games, created = Games.objects.get_or_create(year=row["Year"], city=city)
    # GEt or create sport
    sport, created = Sport.objects.get_or_create(sport_name=row["Sport"])
    # Get or create Discipline
    discipline, created = Discipline.objects.get_or_create(
        discipline_name=row["Discipline"], sport=sport
    )
    # Get or create event
    event, created = Event.objects.get_or_create(
        event_name=row["Event"], discipline=discipline
    )

    # Get country
    country = Country.objects.get(
        country_code=row.get("Country"),
    )
    # Get or create athlete
    gender = row["Gender"].upper()
    athlete, created = Athlete.objects.get_or_create(
        athlete_name=row["Athlete"], gender=gender, country=country
    )

    # Get or create medal
    medal_type = row["Medal"].upper()

    medal, created = MedalWin.objects.get_or_create(
        athlete=athlete, event=event, games=games, medal_type=medal_type
    )

    return medal, created


class Command(BaseCommand):
    """
    Populates the database with countries from a CSV file
    """

    help = "Populates and/or updates the database with Medal information from a relevant CSV file."

    def add_arguments(self, parser):
        parser.add_argument("--file_path", required=True, type=str)

    @transaction.atomic
    def handle(self, file_path=None, *args, **options):
        """
        Built-in django management command callback.

        Atomic transaction to ensure we don't partially update data
        """

        if not isfile(file_path):
            raise CommandError(f"The path {file_path} does not contain a file.")

        medals_created = 0
        with open(file_path) as fhand:
            csv_data = DictReader(fhand)
            for row in csv_data:
                _, created = process_medal_row(row)
                if created:
                    medals_created += 1
                    logger.info(
                        f"{row['Year']} {row['Athlete']} {row['Event']} created"
                    )

        logger.info(f"Medals created: {medals_created}")
