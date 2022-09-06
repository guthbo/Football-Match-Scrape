from django.urls import path
from .views import ChampionatViews, TeamViews, MatchesViews

urlpatterns = [
    path("championat/", ChampionatViews.as_view()),
    path("team/", TeamViews.as_view()),
    path("match/", MatchesViews.as_view()),
]
