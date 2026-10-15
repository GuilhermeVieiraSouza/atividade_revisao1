from django.contrib import admin

from eventos.models import Local, Categoria, Evento, Atividade, Inscricao, Relatorio

# Register your models here.

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'capacidade',)
    search_fields = ('nome', 'endereco')
    
admin.site.register(Categoria)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'inicio', 'local',)
    list_filter = ('local', 'categoria')
    search_fields = ('titulo', 'descricao')
    filter_horizontal = ('categoria', )
    autocomplete_fields = ['local', ]

admin.site.register(Atividade)
admin.site.register(Inscricao)
admin.site.register(Relatorio)

