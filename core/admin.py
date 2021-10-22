from django.contrib import admin
from core.models import Produto

# Register your models here.


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ncm', 'valor', 'data_criacao')
    list_filter = ('usuario', 'nome',)


admin.site.register(Produto, ProdutoAdmin)

