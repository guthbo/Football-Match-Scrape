from django.urls import path
from .views import (
    ChampionatViews,
    TeamViews,
    MatchesViews,
    SingleChampionat,
    SingleMatch,
    SingleTeam,
)

urlpatterns = [
    path("championat/", ChampionatViews.as_view()),
    path("championat/<int:id>/", SingleChampionat.as_view()),
    path("team/", TeamViews.as_view()),
    path("team/<int:id>/", SingleTeam.as_view()),
    path("match/", MatchesViews.as_view()),
    path("match/<int:id>/", SingleTeam.as_view()),
]
