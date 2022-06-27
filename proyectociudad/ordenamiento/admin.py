from django.contrib import admin

# Register your models here.
from ordenamiento.models import *

class ParroquiaAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'tipo_parroquia')
    search_fields = ('nombre',)

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'num_viviendas', 'num_parques', 'num_edificios', 'parroquia')
    raw_id_fields = ('parroquia',)

admin.site.register(Barrio, BarrioAdmin)
