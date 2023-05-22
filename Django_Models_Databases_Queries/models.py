from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView


class Teachers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name} teaches {self.subject}"

    def home_view(request):
        return render(request, 'classroom/home.html')

    class HomeView(TemplateView):
        template_name = 'classroom/home.html'

