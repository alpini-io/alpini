from django.contrib import admin
from .models import Pagina

# Register your models here.

class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'aggiornamento')
    ordering = ('titolo',)
    search_fields = ('titolo',)

admin.site.register(Pagina, PaginaAdmin)