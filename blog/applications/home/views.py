import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

# apps entrada
from applications.entrada.models import Entry
# models
from .models import Home
# forms
from .forms import SuscribersForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # cargamos el home
        # .lastest trae el uultimo registro
        context["home"] = Home.objects.latest('created')  
        # contexto en portada
        context["portada"] = Entry.objects.entrada_en_portada()     
        # contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()   
        # entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes() 
        # enviamos formulario de suscripcion
        context["form"] = SuscribersForm
        return context
    
    

class SuscribersCreateView(CreateView):
  form_class = SuscribersForm
  success_url = '.' 

