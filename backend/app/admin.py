from django.contrib import admin
from .models import Processo, Advogado

@admin.register(Advogado)
class AdvogadoAdmin(admin.ModelAdmin):
    list_display = (
        'advogado_nome',
        'advogado_oab',
    )

@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    list_display = (
        'numero_processo',
        'data_processo',
        'classe_processo',
        'assunto_principal',
        'data_recebimento'
        'vara'
    )