from rest_framework.generics import ListAPIView
from django.db.models import Q, Count

from olympic_data.models import Country, MedalWin
from olympic_data.serializers import CountryMedalSerializer
from olympic_data.models import Games
from rest_framework import status
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
        return Country.objects.all().annotate(
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

    def list(self, request, year):
        if not Games.objects.filter(year=year).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return super().list(request, year)
