from rest_framework.serializers import ModelSerializer
from .models import Championat, Team, Matches


class ChampionatSerializer(ModelSerializer):
    class Meta:
        model = Championat
        fields = "__all__"


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class MatchesSerializer(ModelSerializer):
    class Meta:
        model = Matches
        fields = "__all__"
