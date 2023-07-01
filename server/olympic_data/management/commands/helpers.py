from django.core.management.base import CommandError


def check_required_present(row: dict, key: str):
    """
    Raise an error if a row is missing key fields
    """
    if not row.get(key):
        raise CommandError(f"Row missing {key}", row)
