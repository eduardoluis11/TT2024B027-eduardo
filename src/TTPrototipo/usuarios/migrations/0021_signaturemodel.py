# Generated by Django 5.1.2 on 2024-11-28 17:43

import jsignature.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0020_alter_contrato_archivo_contrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignatureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', jsignature.fields.JSignatureField()),
            ],
        ),
    ]
