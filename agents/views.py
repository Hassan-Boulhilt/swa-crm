from django.shortcuts import render
from django.views import generic
from leads.models import Agent


class AgentsListView(generic.ListView):
    model = Agent
    template_name = "agents/agent_list.html"
