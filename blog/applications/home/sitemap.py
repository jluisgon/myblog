from datetime import timedelta, datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy

# importar todos los modelos (que tengan urls) que deben integrar el sitemap
from applications.entrada.models import Entry


class EntrySitemap(Sitemap):
    # con que frecuencia hacemos los cambios en las urls
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'https'

    # sobreescribir, items que van a generar esto (un conjunto de urls)

    def items(self):
        return Entry.objects.filter(public=True)

    # ordernarlo por orden cronologico (fecha de creacion)
    def lastmosd(self, obj):
        return obj.created

# sobreescribir
class Sitemap(Sitemap):
    # protocolo que estara basado el sitemap (mas recomendable que http)
    protocol = 'https'

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse_lazy(obj)
