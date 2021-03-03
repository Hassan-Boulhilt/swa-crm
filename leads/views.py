from django.core.mail import send_mail
from django.shortcuts import redirect, render, reverse
from .models import Agent, Lead, User
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from django.views import generic


class SignupView(generic.CreateView):

    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login-page")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadsListView(generic.ListView):
    model = Lead
    template_name = "leads/leads_list.html"
    # queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(generic.DetailView):
    model = Lead
    template_name = "leads/lead_detail.html"
    # queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(generic.CreateView):
    model = Lead
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


class LeadUpdateView(generic.UpdateView):
    model = Lead
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")


class LeadDeleteView(generic.DeleteView):
    model = Lead
    template_name = "leads/lead_delete.html"

    def get_success_url(self):
        return reverse("leads:lead_list")


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
