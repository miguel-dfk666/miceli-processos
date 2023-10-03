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
                numero_processo=linha['Número'],
                descricao=linha['Descrição'],
                data_cadastro=linha['Data Cadastro'],
                juiz_responsavel=linha['Juiz Responsável'],
                coligacao=linha['Coligação'],
                numero_dossie=linha['Nº Do Dossiê'],
                pasta_antiga=linha['Pasta Antiga'],
                tipo_de_acao=linha['Tipo De Ação'],
                obj_padrao=linha['Objeto Padrão'],
                advogado_adverso=linha['Advogado Adverso'],
                advogado_agressor=linha['Advogado Agressor'],
                advogado_adverso_numero_oab=linha['Número OAB Advogado Adverso'],
                advogado_colaborador=linha['Advogado Colaborador'],
                advogado_colaborador_numero_oab=linha['Número OAB Advogado Colaborador'],
                tipo_sentenca=linha['Tipo Sentença'],
                data_sentenca=linha['Data Sentença'],
                descricao_sentenca=linha['Descrição Sentença'],
                tipo_acordo=linha['Tipo Acordo'],
                data_acordo=linha['Data Acordo'],
                descricao_acordo=linha['Descrição Acordo'],
                valor_estimado=linha['Valor Estimado'],
                valor_contingencia=linha['Valor Contingência'],
                valor_causa=linha['Valor Causa'],
                valor_pedido=linha['Valor Pedido'],
                valor_risco_provavel=linha['Valor Risco Provável'],
                data_atualizacao=linha['Data Atualização'],
                data_estimada_prevista=linha['Data Estimada Prevista'],
                data_estimada_pagamento=linha['Data Estimada Pagamento'],
                valor_risco=linha['Valor Risco'],
                risco=linha['Risco'],
                total_pago=linha['Total Pago'],
                inss_empresa=linha['INSS Empresa'],
                honorarios=linha['Honorários'],
                custas_processuais=linha['Custas Processuais'],
                situacao=linha['Situação'],
                nome_desdobramento=linha['Nome Desdobramento'],
                data_ajuizamento=linha['Data Ajuizamento'],
                ult_desdobramento=linha['Último Desdobramento'],
                instancia=linha['Instância'],
                rito=linha['Rito'],
                juizo=linha['Juízo'],
                orgao=linha['Órgão'],
                comarca=linha['Comarca'],
                uf=linha['UF'],
                numero=linha['Número'],
                cliente=linha['Cliente'],
                condicao_cliente=linha['Condição Cliente'],
                parte_adversa=linha['Parte Adversa'],
                condicao_adversa=linha['Condição Adversa'],
                cpf_cnpj_adversa=linha['CPF/CNPJ (Adversa)'],
                autor_contumaz=linha['Autor Contumaz'],
                motivo_desligamento=linha['Motivo Desligamento'],
                cargo=linha['Cargo'],
                terceiro_interessado=linha['Terceiro Interessado'],
                terceiro=linha['Terceiro'],
                terceiro_prestador=linha['Terceiro Prestador'],
                cpf_cnpj_terceiro_prestador=linha['CPF/CNPJ (Terc.Prestador)'],
                advogado_credenciado=linha['Adv. Cred.'],
                handle_perito=linha['Handle Perito'],
                perito=linha['Perito'],
                data_encerramento=linha['Data Encerramento'],
                motivo_encerramento=linha['Motivo Encerramento'],
                exito=linha['Êxito'],
                id_benner=linha['ID Benner'],
                data_evento=linha['Data Evento'],
                evento=linha['Evento'],
                tarefas=linha['Tarefas'],
                advogado_centralizador=linha['Adv Centralizador'],
                valor_risco_remoto=linha['Valor Risco Remoto'],
                observacao=linha['Observação'],
                data_atualizada=linha['Data Atualizada'],
            )
            processo.save()
