from django.shortcuts import render
from django.views.generic import TemplateView, FormView


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class ContractFormView(FormView):
    pass
