from django.contrib import admin
from .models import Processo

@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    list_display = (
        'data_processo',
        'numero_processo',
        'advogado_nome',
        'advogado_oab',
        'classe_processo',
        'assunto_principal',
        'data_recebimento',
        'vara',
    )
