from django.contrib import admin
from .models import Categoria, Localizacao, Patrimonio

# Register your models here.
@admin.register(Patrimonio)
class PatrimonioAdmin(admin.ModelAdmin):
    list_display = ('numero_tombamento', 'nome', 'categoria', 'localizacao', 'estado')
    search_fields = ('nome', 'numero_tombamento')
    list_filter = ('estado', 'categoria', 'localizacao')

admin.site.register(Categoria)
admin.site.register(Localizacao)