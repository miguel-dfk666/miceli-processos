# Generated by Django 4.2.5 on 2023-11-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_adv_adverso_processo_advogado_nome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo',
            name='dano_materia',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='dano_moral',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='extincao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='homologacao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='improcedente',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='litigancia',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='procedencia',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='valor_acao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='valor_processo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='processo',
            name='vara_processo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
