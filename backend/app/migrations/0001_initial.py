# Generated by Django 4.2.5 on 2023-10-02 14:29

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Processo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "numero_processo",
                    models.CharField(max_length=20, null=True, unique=True),
                ),
                ("descricao", models.TextField(null=True)),
                ("data_cadastro", models.DateField(default=django.utils.timezone.now)),
                ("juiz_responsavel", models.CharField(max_length=100)),
                ("coligacao", models.CharField(max_length=100, null=True)),
                ("numero_dossie", models.CharField(max_length=25, null=True)),
                ("pasta_antiga", models.CharField(max_length=100, null=True)),
                ("tipo_de_acao", models.CharField(max_length=100, null=True)),
                ("obj_padrao", models.CharField(max_length=100, null=True)),
                ("advogado_adverso", models.CharField(max_length=100, null=True)),
                ("advogado_agressor", models.CharField(max_length=5, null=True)),
                (
                    "advogado_adverso_numero_oab",
                    models.CharField(
                        max_length=10,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="O número da OAB deve estar no formato correto (XXXX/UF). Exemplo: 1234/AB.",
                                regex="^\\d{4,6}/\\w+$",
                            )
                        ],
                    ),
                ),
                ("advogado_colaborador", models.CharField(max_length=100, null=True)),
                (
                    "advogado_colaborador_numero_oab",
                    models.CharField(
                        max_length=10,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="O número da OAB deve estar no formato correto (XXXX/UF). Exemplo: 1234/AB.",
                                regex="^\\d{4,6}/\\w+$",
                            )
                        ],
                    ),
                ),
                ("tipo_sentenca", models.CharField(max_length=65, null=True)),
                ("data_sentenca", models.DateField(default=django.utils.timezone.now)),
                ("descricao_sentenca", models.TextField(null=True)),
                ("tipo_acordo", models.CharField(max_length=65, null=True)),
                ("data_acordo", models.DateField(default=django.utils.timezone.now)),
                ("descricao_acordo", models.TextField(null=True)),
                (
                    "valor_estimado",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "valor_contingencia",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "valor_causa",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "valor_pedido",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "valor_risco_provavel",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("data_estimada_prevista", models.DateField(null=True)),
                ("data_estimada_pagamento", models.DateField(null=True)),
                (
                    "valor_risco",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("risco", models.CharField(max_length=100, null=True)),
                (
                    "total_pago",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "inss_empresa",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "honorarios",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "custas_processuais",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("situacao", models.CharField(max_length=100, null=True)),
                ("nome_desdobramento", models.CharField(max_length=100, null=True)),
                ("data_ajuizamento", models.DateField(null=True)),
                ("ult_desdobramento", models.CharField(max_length=100, null=True)),
                ("instancia", models.CharField(max_length=100, null=True)),
                ("rito", models.CharField(max_length=100, null=True)),
                ("juizo", models.CharField(max_length=100, null=True)),
                ("orgao", models.CharField(max_length=100, null=True)),
                ("comarca", models.CharField(max_length=100, null=True)),
                ("uf", models.CharField(max_length=2, null=True)),
                ("numero", models.CharField(max_length=20, null=True)),
                ("cliente", models.CharField(max_length=100, null=True)),
                ("condicao_cliente", models.CharField(max_length=100, null=True)),
                ("parte_adversa", models.CharField(max_length=100, null=True)),
                ("condicao_adversa", models.CharField(max_length=100, null=True)),
                (
                    "cpf_cnpj_adversa",
                    models.CharField(
                        max_length=18,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="CPF/CNPJ deve conter apenas números e ter 11 ou 14 dígitos.",
                                regex="^\\d{11,14}$",
                            )
                        ],
                    ),
                ),
                ("autor_contumaz", models.CharField(max_length=50, null=True)),
                ("motivo_desligamento", models.TextField(null=True)),
                ("cargo", models.CharField(max_length=100, null=True)),
                ("terceiro_interessado", models.CharField(max_length=50, null=True)),
                ("terceiro", models.CharField(max_length=100, null=True)),
                ("terceiro_prestador", models.CharField(max_length=50, null=True)),
                (
                    "cpf_cnpj_terceiro_prestador",
                    models.CharField(
                        max_length=18,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="CPF/CNPJ deve conter apenas números e ter 11 ou 14 dígitos.",
                                regex="^\\d{11,14}$",
                            )
                        ],
                    ),
                ),
                ("advogado_credenciado", models.CharField(max_length=100, null=True)),
                ("handle_perito", models.CharField(max_length=100, null=True)),
                ("perito", models.CharField(max_length=100, null=True)),
                ("data_encerramento", models.DateField(null=True)),
                ("motivo_encerramento", models.TextField(null=True)),
                ("exito", models.CharField(max_length=100, null=True)),
                ("id_benner", models.CharField(max_length=100, null=True)),
                ("data_evento", models.DateField(null=True)),
                ("evento", models.CharField(max_length=100, null=True)),
                ("tarefas", models.TextField(null=True)),
                ("advogado_centralizador", models.CharField(max_length=100, null=True)),
                (
                    "valor_risco_remoto",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("observacao", models.TextField(null=True)),
                (
                    "data_atualizacao",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
