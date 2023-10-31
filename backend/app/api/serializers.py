from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from app.models import Processo, CustomUser
from django.db.models import Q

class CustomLoginUserSerializer(serializers.ModelSerializer):
   username_or_email = serializers.CharField(required=True)
   password = serializers.CharField(required=True, write_only=True)
   class Meta:
        model = CustomUser
        fields = ['username_or_email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
       }

   def validate(self, data):
      username_or_email = data.get('username_or_email')
      password = data.get('password')

      if username_or_email and password:
         user = CustomUser.objects.filter(Q(email=username_or_email) | Q(username_or_email)).first()

         if user and user.check_password(password):
            return user
         else: 
            raise serializers.ValidationError("Credenciais inválidas")
      else:
         raise serializers.ValidationError("Necessário fornecer um nome de usuário ou email e senha")

class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("As senhas não coincidem.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return CustomUser.objects.create_user(**validated_data)

class PostSerializer(ModelSerializer):
  class Meta:
    model = Processo
    fields = (
        'data_cadastro',
        'numero_dossie',
        'pasta_antiga',
        'natureza',
        'empresa_origem',
        'coligacao',
        'agencia_departamento',
        'area',
        'tipo_de_acao',
        'obj_padrao',
        'fase',
        'inserido_por',
        'alterado_por',
        'data_alt',
        'palavra_chave',
        'valor_estimado',
        'valor_contingencia',
        'valor_causa',
        'valor_pedido',
        'valor_risco_possivel',
        'valor_risco_provavel',
        'risco_provavel_sem_atuacao',
        'valor_contingencia_civel',
        'data_estimada_prevista',
        'data_estimada_pagamento',
        'valor_risco',
        'risco',
        'total_pago',
        'inss_empresa',
        'honorarios',
        'custas_processuais',
        'situacao',
        'nome_desdobramento',
        'data_ajuizamento',
        'ult_desdobramento',
        'instancia',
        'rito',
        'juizo',
        'orgao',
        'comarca',
        'uf',
        'numero',
        'cliente',
        'condicao_cliente',
        'parte_adversa',
        'condicao_adversa',
        'cpf_cnpj_adversa',
        'autor_contumaz',
        'motivo_desligamento',
        'cargo',
        'terceiro_interessado',
        'terceiro',
        'terceiro_prestador',
        'cpf_cnpj_terceiro_prestador',
        'advogado_credenciado',
        'advogado_adverso',
        'advogado_adverso_numero_oab',
        'advogado_agressor',
        'handle_perito',
        'perito',
        'data_encerramento',
        'motivo_encerramento',
        'exito',
        'id_benner',
        'data_evento',
        'evento',
        'tarefas',
        'advogado_centralizador',
        'valor_risco_remoto',
        'observacao',
        'data_atualizacao',
        'alterado_por_auditor',
        'data_alteracao_auditor',
        'danos',
        'assunto',
        'responsabilidade',
        'causas_especiais',
        'solicitacao_encerramento_em',
        'pendencias',
        'inserido_por_evento',
        'percentual_controlador',
        'percentual_ex_controlador',
        'revisao',
        'solicitacao_encerramento_por',
        'tipo_desligamento',
        'advogado_colaborador',
        'advogado_colaborador_numero_oab',
        'equipe',
        'data_do_fato',
        'data_alteracao_fase',
        'subarea',
        'encerrado_em',
        'encerrado_por',
        'valor_acordo',
        'rede',
        'regional',
        'canal_de_contratacao',
        'valor_condenacao_atual',
        'valor_encerramento',
        'valor_contabil_geral',
        'diferenca_encerramento',
        'percentual_diferenca_encerramento',
        'indice_atualizacao',
        'tribunal',
    )