from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict
from teams.models import Team


class TeamView(APIView):
    def post(self, request: Request):
        team_data = request.data
        team = Team.objects.create(**team_data)

        return Response(model_to_dict(team), status=status.HTTP_201_CREATED)

    def get(self, request: Request):
        teams = Team.objects.all()
        teams_dict = [model_to_dict(team) for team in teams]

        return Response(teams_dict, status=status.HTTP_200_OK)
