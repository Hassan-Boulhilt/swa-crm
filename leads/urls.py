from leads.views import (
    AssignAgentView, CategoryCreateView, CategoryDeleteView,
    CategoryDetailView,
    CategoryLeadUpdate,
    CategoryListView, CategoryUpdateView,
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
    path('create-category/', CategoryCreateView.as_view(), name="category-create"),
    path('update-category/<pk>/',
         CategoryUpdateView.as_view(), name="category-update"),
    path('delete-category/<pk>/',
         CategoryDeleteView.as_view(), name="category-delete"),



]
