
from django.db import models

class EntryManager(models.Manager):
    # procedimiento para entrada
    
    def entrada_en_portada(self):
        return self.filter(
            public = True,
            portada = True,            
        ).order_by('-created').first()    
    
    def entradas_en_home(self):
        # devuelve las ultimas cuatro entradas en home
        return self.filter(
            public = True,
            in_home = True,            
        ).order_by('-created')[:4]

    def entradas_recientes(self):
        # devuelve las ultimas seis entradas recientes
        return self.filter(
            public = True,                   
        ).order_by('-created')[:6]
