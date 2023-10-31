from django.core.management.base import BaseCommand
import pandas as pd
from app.models import Processo

class Command(BaseCommand):
    help = 'Importa dados do Excel para o banco de dados'
    
    def handle(self, *args, **kwargs):
        caminho_do_arquivo_excel = r'C:\Users\miguel.silva\Downloads\nova_planilha.xlsx'
        dados_excel = pd.read_excel(caminho_do_arquivo_excel, engine='openpyxl')
        
        for _, linha in dados_excel.iterrows():
            processo = Processo(
                data_processo=linha['data_processo'], 
                numero_processo=linha['numero_processo'],
                advogado_nome=linha['advogado_nome'],
                advogado_oab=linha['advogado_oab'],
                classe_processo=linha['classe_processo'],
                assunto_principal=linha['assunto_principal']
                data_recebimento=linha['data_recebimento'],
                vara=linha['vara']
            )
            processo.save()
