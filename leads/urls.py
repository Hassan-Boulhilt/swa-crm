from leads.views import (
    AssignAgentView,
    CategoryDetailView,
    CategoryLeadUpdate,
    CategoryListView,
    LeadCreateView,
    LeadDeleteView,
    LeadDetailView,
    LeadUpdateView,
    LeadsListView,
)
from django.urls import path

app_name = "leads"
urlpatterns = [
    path('', LeadsListView.as_view(), name='lead_list'),
    path('detail/<pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('update/<pk>/', LeadUpdateView.as_view(), name='lead_update'),
    path('delete/<pk>/', LeadDeleteView.as_view(), name="lead_delete"),
    path('assign-agent/<pk>/', AssignAgentView.as_view(), name='assign_agent'),
    path('category/<pk>/',
         CategoryLeadUpdate.as_view(), name='lead-category-update'),
    path('create/', LeadCreateView.as_view(), name='lead_create'),
    path('categories/', CategoryListView.as_view(), name="category-list"),
    path('categories/<pk>/', CategoryDetailView.as_view(), name="category-detail"),



]
