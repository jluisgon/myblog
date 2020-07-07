"""
Proyecto Curso Django
"""
from django.contrib import admin
from django.urls import path, re_path, include

# setting 
from django.conf import settings
from django.conf.urls.static import static
# SEO
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import (
    EntrySitemap,
    Sitemap,
)

# comentado por SEO
#urlpatterns = [
urlpatterns_main = [ 
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.entrada.urls')),
    re_path('', include('applications.favoritos.urls')),
    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
    
    # para que cargen las imganes en el navegador
]  + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

#objeto site map que genera xml
sitemaps = {
    'site':Sitemap(
        [    # se crea la url raiz a partir de aca 
            'home_app:index'
        ]
    ),
    # urls secundarias que parte de la url raiz
    'entradas': EntrySitemap
}

# crear las url generadas
urlpatterns_sitemap = [
    path(
        'sitemap.xml', 
        sitemap, 
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    )
]

urlpatterns = urlpatterns_main + urlpatterns_sitemap