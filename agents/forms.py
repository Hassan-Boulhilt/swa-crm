from django import forms
from leads.models import Agent


class AgentModelFormForm(forms.ModelForm):

    class Meta:
        model = Agent
        fields = ("user",)
