from agents.views import AgentCreateView, AgentDetailView, AgentListView
from django.urls import path


app_name = "agents"

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('detail/<pk>', AgentDetailView.as_view(), name='agent-detail'),
    path('create/', AgentCreateView.as_view(), name='agent-create')
]
