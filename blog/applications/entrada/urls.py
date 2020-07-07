#
from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path(
        'entradas/', 
        views.EntryListView.as_view(),
        name='entry-lista',
    ),   
    path(
        # 'entrada/<pk>/', 
        # para el SEO, el slug busca un slog dentro del model y recupera el archivo tal como lo hace el pk
        # por eso es que debe ser unico
        'entrada/<slug>/', 
        views.EntryDetailView.as_view(),
        name='entry-detail',
    ),   
]