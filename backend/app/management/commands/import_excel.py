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
                numero_processo = linha['Numero do Processo'],
                advogado = linha['Advogado'],
                classe_do_processo = linha['Classe do Processo'],
                assunto_principal = linha['Assunto Principal'],
                data_recebimento = linha['Data Recebimento'],
                vara = linha['Vara'],
            )
            processo.save()
