# Generated by Django 4.2.5 on 2023-10-03 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_processo_tribunal"),
    ]

    operations = [
        migrations.AddField(
            model_name="processo",
            name="adv_adverso",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="adv_agressor",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="agencia_departamento",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="alterado_por",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="alterado_por_auditor",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="area",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="assunto",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="canal_de_contratacao",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="causas_especiais",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="danos",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="data_alt",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="processo",
            name="data_alteracao_auditor",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="data_alteracao_fase",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="data_do_fato",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="diferenca_encerramento",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="empresa_origem",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="encerrado_em",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="encerrado_por",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="equipe",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="fase",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="indice_atualizacao",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="inserido_por",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="inserido_por_evento",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="natureza",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="palavra_chave",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="pendencias",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="percentual_controlador",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name="processo",
            name="percentual_diferenca_encerramento",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name="processo",
            name="percentual_ex_controlador",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name="processo",
            name="rede",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="regional",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="responsabilidade",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="revisao",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="risco_provavel_sem_atuacao",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="solicitacao_encerramento_em",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="solicitacao_encerramento_por",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="subarea",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="tipo_desligamento",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="valor_acordo",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="valor_condenacao_atual",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="valor_contabil_geral",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="valor_contingencia_civel",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="valor_encerramento",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="valor_risco_possivel",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="processo",
            name="advogado_agressor",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="processo",
            name="tipo_de_acao",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="processo",
            name="tribunal",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
