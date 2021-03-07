from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from leads.models import Agent
from .forms import AgentModelFormForm


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Agent
    template_name = "agents/agent_create.html"
    form_class = AgentModelFormForm

    def get_success_url(self):
        return reverse('agents:agent-list')


class AgentListView(LoginRequiredMixin, generic.ListView):
    model = Agent
    template_name = "agents/agent_list.html"

    context_object_name = "agents"


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Agent
    template_name = "agents/agent_detail.html"

    context_object_name = "agents"
