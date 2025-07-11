# Generated by Django 5.2.4 on 2025-07-06 23:08

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('doc_identificacao', models.CharField(max_length=18, unique=True, verbose_name='Documento (CPF ou CNPJ)')),
                ('nome_produtor', models.CharField(max_length=255, verbose_name='Nome do produtor')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email do produtor')),
                ('telefone', models.CharField(max_length=255, verbose_name='Principal Contato do produtor')),
            ],
        ),
        migrations.CreateModel(
            name='Safra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20, verbose_name='Safra')),
            ],
        ),
        migrations.CreateModel(
            name='PropriedadeRural',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_fazenda', models.CharField(max_length=255, verbose_name='Nome da fazenda (propriedade)')),
                ('area_agricultavel', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Área agricultável (ha)')),
                ('area_vegetacao', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Área de vegetação (ha)')),
                ('area_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Área total da fazenda (ha)')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('produtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propriedades', to='rural_producers.produtor')),
            ],
        ),
        migrations.CreateModel(
            name='CulturaPlantada',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_cultura', models.CharField(max_length=100, verbose_name='Cultura plantada')),
                ('propriedade_rural', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='culturas', to='rural_producers.propriedaderural')),
                ('safra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='safra', to='rural_producers.safra')),
            ],
        ),
    ]
