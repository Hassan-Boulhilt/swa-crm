from leads.views import (
    AssignAgentView, LeadCreateView, LeadDeleteView, LeadDetailView, LeadUpdateView,
    LeadsListView,
    lead_create,
    lead_delete,
    lead_detail,
    lead_list,
    lead_update
)
from django.urls import path

app_name = "leads"
urlpatterns = [
    path('', LeadsListView.as_view(), name='lead_list'),
    path('detail/<pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('update/<pk>/', LeadUpdateView.as_view(), name='lead_update'),
    path('delete/<pk>/', LeadDeleteView.as_view(), name="lead_delete"),
    path('assign-agent/<pk>/', AssignAgentView.as_view(), name='assign_agent'),
    path('create/', LeadCreateView.as_view(), name='lead_create'),


]
