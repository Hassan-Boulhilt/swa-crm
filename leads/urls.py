from leads.views import lead_create, lead_detail, lead_list
from django.urls import path

app_name = "leads"
urlpatterns = [
    path('', lead_list, name='lead_list'),
    path('detail/<id>', lead_detail, name='lead_detail'),
    path('create/', lead_create, name='lead_create'),
]
