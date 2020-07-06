from django.shortcuts import render


from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# esta vista solo la podran ver solo usuarios logeados
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    View,
    DeleteView
)

from applications.entrada.models import Entry

from .models import Favorites

# Create your views here.

class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'
    login_url =  ('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)


class AddFavoritosView(LoginRequiredMixin, View):
    login_url =  ('users_app:user-login')
    
    def post (self, request, *args, **kwargs):
        # recuperar el usuario
        usuario = self.request.user
        entrada = Entry.objects.get(id = self.kwargs['pk'])
        # registamos favoritos
        Favorites.objects.create(
            user= usuario,
            entry = entrada        
        )
        
        return HttpResponseRedirect (
            reverse(
                'favoritos_app:perfil'
            )
        )        

class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favoritos_app:perfil')
       
