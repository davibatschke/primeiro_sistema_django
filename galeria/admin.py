from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicacao')
    list_display_links = ('id', 'nome')
    search_fields = ['nome']
    list_filter = ['categoria']
    list_per_page = 10

# Register your models here.
admin.site.register(Fotografia, ListandoFotos)