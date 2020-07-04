from django.db import models

# para el foreingkey de user en entry
from django.conf import settings


# apps de tercero
from model_utils.models import TimeStampedModel

from applications.entrada.models import Entry

# Create your models here.

class Favorites(TimeStampedModel):
    """ modelo para favoritos """
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name = 'user_favorites',
        on_delete=models.CASCADE
    )
    
    entry = models.ForeignKey(
        Entry, 
        related_name = 'entry_favorites',
        on_delete=models.CASCADE
    )    
    
    class Meta:
        unique_together = ('user', 'entry')    
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = 'Entradas Favoritas'
        
    def __str__(self):
        return self.entry.title
    
    
    
