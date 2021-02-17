from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import os


class HomeView(TemplateView):
    template_name = 'home.html'