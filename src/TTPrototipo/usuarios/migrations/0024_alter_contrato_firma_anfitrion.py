# Generated by Django 5.1.2 on 2024-11-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0023_alter_signaturemodel_file_alter_signaturemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='firma_anfitrion',
            field=models.ImageField(blank=True, null=True, upload_to='firmas/firmas_anfitriones/'),
        ),
    ]