from django.db.models import Case, Count, F, FloatField, Q, When
from olympic_data.models import Country, Games, MedalWin
from olympic_data.serializers import CountryMedalSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class MedalTableView(ListAPIView):
    """
    Returns all countries in the database with their medal tally, by a year's games.

    Returns 400 for invalid year.
    """

    queryset = Country.objects.all()
    serializer_class = CountryMedalSerializer

    def get_queryset(self):
        year = self.kwargs["year"]
        return (
            Country.objects.all()
            .annotate(
                gold_medals=Count(
                    "medalwin",
                    filter=Q(
                        medalwin__games__year=year,
                        medalwin__medal_type=MedalWin.Medals.GOLD,
                    ),
                ),
                silver_medals=Count(
                    "medalwin",
                    filter=Q(
                        medalwin__games__year=year,
                        medalwin__medal_type=MedalWin.Medals.SILVER,
                    ),
                ),
                bronze_medals=Count(
                    "medalwin",
                    filter=Q(
                        medalwin__games__year=year,
                        medalwin__medal_type=MedalWin.Medals.BRONZE,
                    ),
                ),
            )
            .annotate(
                population_per_gold_medal=Case(
                    When(gold_medals__gte=1.0, then=F("population") / F("gold_medals")),
                    default=0,
                    output_fields=FloatField(),
                ),
                population_per_silver_medal=Case(
                    When(
                        silver_medals__gte=1.0,
                        then=F("population") / F("silver_medals"),
                    ),
                    default=0,
                    output_fields=FloatField(),
                ),
                population_per_bronze_medal=Case(
                    When(
                        bronze_medals__gte=1.0,
                        then=F("population") / F("bronze_medals"),
                    ),
                    default=0,
                    output_fields=FloatField(),
                ),
            )
        )

    def list(self, request, year):
        if not Games.objects.filter(year=year).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return super().list(request, year)


# Medals per population

# Per games
# All 3 types of medals
# population /


def get_by_population(year: int):
    """
    :return: country object {"country_name": "Argentina", "population_per_gold_medal":50}
    """

    return (
        Country.objects.all()
        .annotate(
            gold_medals=Count(
                "medalwin",
                filter=Q(
                    medalwin__games__year=year,
                    medalwin__medal_type=MedalWin.Medals.GOLD,
                ),
            ),
            silver_medals=Count(
                "medalwin",
                filter=Q(
                    # medalwin__games__year=year,
                    medalwin__medal_type=MedalWin.Medals.SILVER,
                ),
            ),
            bronze_medals=Count(
                "medalwin",
                filter=Q(
                    # medalwin__games__year=year,
                    medalwin__medal_type=MedalWin.Medals.BRONZE,
                ),
            ),
        )
        .annotate(
            population_per_gold_medal=F("population") / F("gold_medals"),
            population_per_silver_medal=F("population") / F("silver_medals"),
            population_per_bronze_medal=F("population") / F("bronze_medals"),
        )
    )
