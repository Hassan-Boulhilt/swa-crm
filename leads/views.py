from django.core.mail import send_mail
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Agent, Category, Lead, User
from .forms import AssignAgentForm, LeadForm, LeadModelForm, CustomUserCreationForm
from django.views import generic
from agents.mixins import OrganisorAndLoginRequiredMixin


class SignupView(generic.CreateView):

    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login-page")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadsListView(LoginRequiredMixin, generic.ListView):

    template_name = "leads/leads_list.html"
    # queryset = Lead.objects.all()

    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        # initial queryset for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation=user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            # filter
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(LeadsListView, self).get_context_data(**kwargs)
        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation=user.userprofile, agent__isnull=True)

            context.update({
                "unassigned_leads": queryset
            })
        return context


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    model = Lead
    template_name = "leads/lead_detail.html"
    # queryset = Lead.objects.all()
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        # initial queryset for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            # filter
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):

    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject="A lead has been created",
            message="Go to the site to the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )

        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        # initial queryset for the entire organisation
        queryset = Lead.objects.filter(organisation=user.userprofile)
        return queryset

    def get_success_url(self):
        return reverse("leads:lead_list")


class LeadDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):

    template_name = "leads/lead_delete.html"

    def get_queryset(self):
        user = self.request.user
        # initial queryset for the entire organisation
        queryset = Lead.objects.filter(organisation=user.userprofile)
        return queryset

    def get_success_url(self):
        return reverse("leads:lead_list")


class AssignAgentView(OrganisorAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)


class CategoryListView(LoginRequiredMixin, generic.ListView):

    template_name = "category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):

        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user

        # get all leads that belong to the organisor
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            # get leads that belong to a specifique agent
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)

        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        # get all leads categories belong to the organisor
        if user.is_organisor:
            queryset = Category.objects.filter(organisation=user.userprofile)
        else:
            # get the leads categories belong to a specifique agent
            queryset = Category.objects.filter(
                organisation=user.agent.organisation)

        return queryset


def landing_page(request):
    return render(request, "landing.html")


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/leads_list.html", context)


def lead_detail(request, id):
    lead = Lead.objects.get(id=id)
    context = {
        "lead": lead,
    }
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadModelForm()

    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

# def lead_create(request):
#     form = LeadForm()

#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(first_name=first_name,
#                                 last_name=last_name,
#                                 age=age, agent=agent)

#             return redirect("/leads")

#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)


def lead_update(request, id):

    lead = Lead.objects.get(id=id)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
        return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)


# def lead_update(request, id):

#     lead = Lead.objects.get(id=id)
#     form = LeadForm()

#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()

#             return redirect("/leads")

#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, "leads/lead_update.html", context)

def lead_delete(request, id):
    lead = Lead.objects.get(id=id)
    lead.delete()
    return redirect("/leads")
