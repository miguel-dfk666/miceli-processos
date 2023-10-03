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
    natureza = models.CharField(max_length=100, null=True)
    empresa_origem = models.CharField(max_length=255, null=True)
    agencia_departamento = models.CharField(max_length=255, null=True)
    area = models.CharField(max_length=255, null=True)
    tipo_de_acao = models.CharField(max_length=255, null=True)
    obj_padrao = models.CharField(max_length=100, null=True)
    fase = models.CharField(max_length=100, null=True)
    inserido_por = models.CharField(max_length=100, null=True)
    alterado_por = models.CharField(max_length=100, null=True)
    data_alt = models.DateTimeField(default=timezone.now, editable=True)
    palavra_chave = models.CharField(max_length=100, null=True)

    # Informações sobre Advogados
    advogado_adverso = models.CharField(max_length=100, null=True)
    advogado_agressor = models.CharField(max_length=100, null=True)
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

    # Outras Informações
    tipo_sentenca = models.CharField(max_length=65, null=True)
    data_sentenca = models.DateField(default=timezone.now)
    descricao_sentenca = models.TextField(null=True)
    tipo_acordo = models.CharField(max_length=65, null=True)
    data_acordo = models.DateField(default=timezone.now)
    descricao_acordo = models.TextField(null=True)

    # Informações sobre Valores
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_contingencia = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_causa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_risco_provavel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_risco_possivel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    risco_provavel_sem_atuacao = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_contingencia_civel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_estimada_prevista = models.DateField(null=True)
    data_estimada_pagamento = models.DateField(null=True)
    valor_risco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    risco = models.CharField(max_length=100, null=True)
    total_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    inss_empresa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    honorarios = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    custas_processuais = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Informações sobre Sentença e Acordo
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

    # Informações sobre Clientes e Partes Adversas
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

    # Informações sobre Funcionários e Terceiros
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

    # Informações sobre Advogados e Peritos
    advogado_credenciado = models.CharField(max_length=100, null=True)
    adv_adverso = models.CharField(max_length=100, null=True)
    adv_agressor = models.CharField(max_length=100, null=True)
    handle_perito = models.CharField(max_length=100, null=True)
    perito = models.CharField(max_length=100, null=True)

    # Informações sobre Encerramento
    data_encerramento = models.DateField(null=True)
    motivo_encerramento = models.TextField(null=True)
    exito = models.CharField(max_length=100, null=True)
    id_benner = models.CharField(max_length=100, null=True)

    # Informações sobre Eventos e Tarefas
    data_evento = models.DateField(null=True)
    evento = models.CharField(max_length=100, null=True)
    tarefas = models.TextField(null=True)

    # Informações sobre Riscos e Observações
    advogado_centralizador = models.CharField(max_length=100, null=True)
    valor_risco_remoto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    observacao = models.TextField(null=True)

    # Informações sobre Atualizações e Auditoria
    data_atualizacao = models.DateTimeField(default=timezone.now, editable=True)
    alterado_por_auditor = models.CharField(max_length=100, null=True)
    data_alteracao_auditor = models.DateTimeField(null=True)

    # Informações sobre Valores Financeiros e Contabilidade
    danos = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    assunto = models.CharField(max_length=255, null=True)
    responsabilidade = models.CharField(max_length=255, null=True)
    causas_especiais = models.CharField(max_length=255, null=True)
    solicitacao_encerramento_em = models.DateField(null=True)
    pendencias = models.TextField(null=True)
    inserido_por_evento = models.CharField(max_length=100, null=True)
    percentual_controlador = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    percentual_ex_controlador = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    revisao = models.CharField(max_length=255, null=True)
    solicitacao_encerramento_por = models.CharField(max_length=100, null=True)
    tipo_desligamento = models.CharField(max_length=100, null=True)
    advogado_colaborador = models.CharField(max_length=100, null=True)
    equipe = models.CharField(max_length=100, null=True)
    data_do_fato = models.DateField(null=True)
    data_alteracao_fase = models.DateField(null=True)
    subarea = models.CharField(max_length=255, null=True)
    encerrado_em = models.DateField(null=True)
    encerrado_por = models.CharField(max_length=100, null=True)
    valor_acordo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    rede = models.CharField(max_length=255, null=True)
    regional = models.CharField(max_length=255, null=True)
    canal_de_contratacao = models.CharField(max_length=255, null=True)
    valor_condenacao_atual = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_encerramento = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_contabil_geral = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    diferenca_encerramento = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    percentual_diferenca_encerramento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    indice_atualizacao = models.CharField(max_length=255, null=True)
    tribunal = models.CharField(max_length=255, null=True)

    def save(self, *args, **kwargs):
        self.data_atualizacao = timezone.now()
        super(Processo, self).save(*args, **kwargs)

    def __str__(self):
        return self.numero_processo