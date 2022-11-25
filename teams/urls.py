from django.urls import path
from .views import TeamView, TeamByIdView

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamByIdView.as_view()),
]
