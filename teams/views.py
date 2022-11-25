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


class TeamByIdView(APIView):
    def get(self, request: Request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        return Response(model_to_dict(team), status=status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        return Response(model_to_dict(team), status=status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
