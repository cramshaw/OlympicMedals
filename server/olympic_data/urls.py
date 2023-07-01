from django.urls import path

from .views import MedalTableView


urlpatterns = [
    path("medal-table/<int:year>/", MedalTableView.as_view(), name="medal-table"),
]
