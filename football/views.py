from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Championat, Team, Matches
from .serializer import ChampionatSerializer, TeamSerializer, MatchesSerializer
from rest_framework import status

# Create your views here.


class ChampionatViews(APIView):
    def get(self, request):
        all_championats = Championat.objects.all()
        serialized_data = ChampionatSerializer(data=all_championats, many=True)

        serialized_data.is_valid()

        return Response(data=serialized_data.data)

    def post(self, request):
        serialized_data = ChampionatSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data)
        return Response({"Error": serialized_data.errors})

    def delete(self, request):
        id = request.data["id"]
        try:
            Championat.objects.get(id=id).delete()
            return Response({"status": "Success!"}, status=status.HTTP_200_OK)
        except:
            return Response({"status": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        championat = Championat.objects.get(id=request.data["id"])
        serialized_data = ChampionatSerializer(
            championat, data=request.data, partial=True
        )

        if serialized_data.is_valid():
            serialized_data.save()

            return Response(data=serialized_data.data)

        return Response({"Error!": serialized_data.errors})


class SingleChampionat(APIView):
    def get(self, request, id):
        championat_data = Championat.objects.get(id=id)

        return Response(
            data={
                "id": championat_data.id,
                "match": championat_data.match,
                "country": championat_data.country,
                "date": championat_data.date,
            }
        )


class TeamViews(APIView):
    def get(self, request):
        all_teams = Team.objects.all()
        serialized_data = TeamSerializer(data=all_teams, many=True)

        serialized_data.is_valid()

        return Response(data=serialized_data.data)

    def post(self, request):
        serialized_data = TeamSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data)
        return Response({"Error": serialized_data.errors})

    def delete(self, request):
        id = request.data["id"]
        try:
            Team.objects.get(id=id).delete()
            return Response({"status": "Success!"}, status=status.HTTP_200_OK)
        except:
            return Response({"status": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        team = Team.objects.get(id=request.data["id"])
        serialized_data = ChampionatSerializer(team, data=request.data, partial=True)

        if serialized_data.is_valid():
            serialized_data.save()

            return Response(data=serialized_data.data)

        return Response({"Error!": serialized_data.errors})


class SingleTeam(APIView):
    def get(self, request, id):
        team_data = Team.objects.get(id=id)

        return Response(
            data={
                "id": team_data.id,
                "team": team_data.team,
                "logo": team_data.logo,
                "is_guest": team_data.is_guest,
            }
        )


class MatchesViews(APIView):
    def get(self, request):
        all_matches = Matches.objects.all()
        serialized_data = MatchesSerializer(data=all_matches, many=True)

        serialized_data.is_valid()

        return Response(data=serialized_data.data)

    def post(self, request):
        serialized_data = MatchesSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data)
        return Response({"Error": serialized_data.errors})

    def delete(self, request):
        id = request.data["id"]
        try:
            Matches.objects.get(id=id).delete()
            return Response({"status": "Success!"}, status=status.HTTP_200_OK)
        except:
            return Response({"status": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        match = Matches.objects.get(id=request.data["id"])
        serialized_data = ChampionatSerializer(match, data=request.data, partial=True)

        if serialized_data.is_valid():
            serialized_data.save()

            return Response(data=serialized_data.data)

        return Response({"Error!": serialized_data.errors})


class SingleMatch(APIView):
    def get(self, request, id):
        match_data = Matches.objects.get(id=id)

        return Response(
            data={
                "date": match_data.date,
                "score": match_data.score,
                "team_one": match_data.team_one,
                "team_two": match_data.team_two,
            }
        )
