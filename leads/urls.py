from leads.views import lead_create, lead_delete, lead_detail, lead_list, lead_update
from django.urls import path

app_name = "leads"
urlpatterns = [
    path('', lead_list, name='lead_list'),
    path('detail/<id>', lead_detail, name='lead_detail'),
    path('update/<id>', lead_update, name='lead_update'),
    path('delete/<id>', lead_delete, name="lead_delete"),
    path('create/', lead_create, name='lead_create'),

]
