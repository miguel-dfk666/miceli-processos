import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Processo(models.Model):
    # Informações Básicas do Processo
    numero_processo = models.CharField(max_length=20, unique=True, null=True)
    descricao = models.TextField(null=True)
    data_cadastro = models.DateField(default=timezone.now)
    juiz_responsavel = models.CharField(max_length=100)
    coligacao = models.CharField(max_length=100, null=True)
    numero_dossie = models.CharField(max_length=25, null=True)
    pasta_antiga = models.CharField(max_length=100, null=True)
    tipo_de_acao = models.CharField(max_length=100, null=True)
    obj_padrao = models.CharField(max_length=100, null=True)

    # Informações sobre Advogados
    advogado_adverso = models.CharField(max_length=100, null=True)
    advogado_agressor = models.CharField(max_length=5, null=True)
    advogado_adverso_numero_oab = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{4,6}/\w+$',
                message='O número da OAB deve estar no formato correto (XXXX/UF). Exemplo: 1234/AB.',
            ),
        ],
        unique=True,
        null=True
    )
    advogado_colaborador = models.CharField(max_length=100, null=True)
    advogado_colaborador_numero_oab = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{4,6}/\w+$',
                message='O número da OAB deve estar no formato correto (XXXX/UF). Exemplo: 1234/AB.',
            ),
        ],
        unique=True,
        null=True
    )

    # Informações sobre Sentença
    tipo_sentenca = models.CharField(max_length=65, null=True)
    data_sentenca = models.DateField(default=timezone.now)
    descricao_sentenca = models.TextField(null=True)

    # Informações sobre Acordo
    tipo_acordo = models.CharField(max_length=65, null=True)
    data_acordo = models.DateField(default=timezone.now)
    descricao_acordo = models.TextField(null=True)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_contingencia = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_causa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_risco_provavel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_atualizacao = models.DateTimeField(default=timezone.now, editable=True)

    # Informações Adicionais
    data_estimada_prevista = models.DateField(null=True)
    data_estimada_pagamento = models.DateField(null=True)
    valor_risco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    risco = models.CharField(max_length=100, null=True)
    total_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    inss_empresa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    honorarios = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    custas_processuais = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    situacao = models.CharField(max_length=100, null=True)
    nome_desdobramento = models.CharField(max_length=100, null=True)
    data_ajuizamento = models.DateField(null=True)
    ult_desdobramento = models.CharField(max_length=100, null=True)
    instancia = models.CharField(max_length=100, null=True)
    rito = models.CharField(max_length=100, null=True)
    juizo = models.CharField(max_length=100, null=True)
    orgao = models.CharField(max_length=100, null=True)
    comarca = models.CharField(max_length=100, null=True)
    uf = models.CharField(max_length=2, null=True)
    numero = models.CharField(max_length=20, null=True)
    cliente = models.CharField(max_length=100, null=True)
    condicao_cliente = models.CharField(max_length=100, null=True)
    parte_adversa = models.CharField(max_length=100, null=True)
    condicao_adversa = models.CharField(max_length=100, null=True)
    cpf_cnpj_adversa = models.CharField(
        max_length=18,
        validators=[
            RegexValidator(
                regex=r'^\d{11,14}$',
                message='CPF/CNPJ deve conter apenas números e ter 11 ou 14 dígitos.',
            ),
        ],
        null=True
    )
    autor_contumaz = models.CharField(max_length=50, null=True)
    motivo_desligamento = models.TextField(null=True)
    cargo = models.CharField(max_length=100, null=True)
    terceiro_interessado = models.CharField(max_length=50, null=True)
    terceiro = models.CharField(max_length=100, null=True)
    terceiro_prestador = models.CharField(max_length=50, null=True)
    cpf_cnpj_terceiro_prestador = models.CharField(
        max_length=18,
        validators=[
            RegexValidator(
                regex=r'^\d{11,14}$',
                message='CPF/CNPJ deve conter apenas números e ter 11 ou 14 dígitos.',
            ),
        ],
        null=True
    )
    advogado_credenciado = models.CharField(max_length=100, null=True)
    handle_perito = models.CharField(max_length=100, null=True)
    perito = models.CharField(max_length=100, null=True)
    data_encerramento = models.DateField(null=True)
    motivo_encerramento = models.TextField(null=True)
    exito = models.CharField(max_length=100, null=True)
    id_benner = models.CharField(max_length=100, null=True)
    data_evento = models.DateField(null=True)
    evento = models.CharField(max_length=100, null=True)
    tarefas = models.TextField(null=True)
    advogado_centralizador = models.CharField(max_length=100, null=True)
    valor_risco_remoto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    observacao = models.TextField(null=True)
    data_atualizacao = models.DateTimeField(default=timezone.now, editable=True)

    def save(self, *args, **kwargs):
        # Arredondar campos de valor para 2 casas decimais
        # self.valor_estimado = round(self.valor_estimado, 2)
        # self.valor_causa = round(self.valor_causa, 2)
        # self.valor_pedido = round(self.valor_pedido, 2)
        # self.valor_risco_provavel = round(self.valor_risco_provavel, 2)
        # self.valor_risco = round(self.valor_risco, 2)
        # self.total_pago = round(self.total_pago, 2)
        # self.inss_empresa = round(self.inss_empresa, 2)
        # self.honorarios = round(self.honorarios, 2)
        # self.custas_processuais = round(self.custas_processuais, 2)
        # self.valor_risco_remoto = round(self.valor_risco_remoto, 2)

        self.data_atualizacao = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.numero_processo