# from django.core.management.base import BaseCommand
# import pandas as pd
# from app.models import Processo

# class Command(BaseCommand):
#     help = 'Importa dados do Excel para o banco de dados'
    
#     def handle(self, *args, **kwargs):
#       caminho_do_arquivo_excel = 'caminho/para/sua/planilha.xlsx'
#       dados_excel = pd.read_excel(caminho_do_arquivo_excel, engine='openpyxl')
      
#       for _, linha in dados_excel.iterrows():
#         objeto_modelo = Processo(
          
#         )