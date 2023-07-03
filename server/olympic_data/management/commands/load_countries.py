import logging
from csv import DictReader
from os.path import isfile

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from olympic_data.models import Country
from .helpers import check_required_present

logger = logging.getLogger(__name__)


def process_country_row(row: dict):
    """
    Method to check required fields are included and create/update

    :param row: Row of CSV file
    """
    for key in ["Country", "Code"]:
        check_required_present(row, key)

    population = row.get("Population")
    gdp_per_capita = row.get("GDP per Capita")
    defaults = {
        "population": population if population != "" else None,
        "gdp_per_capita": gdp_per_capita if gdp_per_capita != "" else None,
    }

    country, created = Country.objects.update_or_create(
        country_name=row.get("Country").strip("*"),
        country_code=row.get("Code"),
        defaults=defaults,
    )
    return country, created


class Command(BaseCommand):
    """
    Populates the database with countries from a CSV file
    """

    help = "Populates and/or updates the database with Country information from a relevant CSV file."

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

        countries_created = 0
        countries_existant = 0
        with open(file_path) as fhand:
            csv_data = DictReader(fhand)
            for row in csv_data:
                _, created = process_country_row(row)
                country_name = row.get("Country")
                if created:
                    countries_created += 1
                    logger.info(f"Country {country_name} created")
                else:
                    countries_existant += 1
                    logger.info(f"Country {country_name} exists - updated.")

        logger.info(f"Countries created: {countries_created}")
        logger.info(f"Existing Countries: {countries_existant}")
