from django.contrib import admin

# Register your models here.
from .models import Home, Suscribers, Contact

admin.site.register(Home)
admin.site.register(Suscribers)
admin.site.register(Contact)

