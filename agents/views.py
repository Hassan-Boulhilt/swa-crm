import random


from django.core.mail import send_mail
from django.views import generic
from django.shortcuts import render, reverse
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin


class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    model = Agent
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile,
        )
        send_mail(
            subject="You are invited to be an agent",
            message="You were added as an agent by swa-crm, Please come login to start working",
            from_email="test@test.com",
            recipient_list=[user.email]
        )

        # agent.organisation = self.request.user.userprofile
        # agent.save()

        return super(AgentCreateView, self).form_valid(form)


class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    context_object_name = "agents"


class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):

    template_name = "agents/agent_detail.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    context_object_name = "agent"


class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    model = Agent
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")


class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):

    template_name = "agents/agent_delete.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        return reverse("agents:agent-list")
