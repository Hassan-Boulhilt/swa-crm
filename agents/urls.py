from agents.views import AgentCreateView, AgentDeleteView, AgentDetailView, AgentListView, AgentUpdateView
from django.urls import path


app_name = "agents"

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('detail/<pk>', AgentDetailView.as_view(), name='agent-detail'),
    path('update/<pk>', AgentUpdateView.as_view(), name='agent-update'),
    path('delete/<pk>', AgentDeleteView.as_view(), name='agent-delete'),
    path('create/', AgentCreateView.as_view(), name='agent-create'),

]
