from django.shortcuts import render

from django.views.generic import ListView


from .models import Entry, Category

# Create your views here.



class EntryListView(ListView):    
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all()        
        return context    
    
    def get_queryset(self):       
        # recuperar un kword desde un formulario html
        kword = self.request.GET.get('kword', '')
        # va a venir la por url
        categoria = self.request.GET.get('categoria', '')
        # consulta de busqueda
        resultado = Entry.objects.buscar_entrada(kword, categoria)
        return resultado
    
    
