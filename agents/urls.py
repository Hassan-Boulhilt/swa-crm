from agents.views import AgentsListView
from django.urls import path


app_name = "agents"

urlpatterns = [
    path("", AgentsListView.as_view(), name="agent-list"),
]
