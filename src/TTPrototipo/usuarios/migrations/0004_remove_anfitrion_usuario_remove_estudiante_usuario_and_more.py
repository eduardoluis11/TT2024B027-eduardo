# Generated by Django 5.1.2 on 2024-11-11 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_anfitrion_contratos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anfitrion',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='anfitrion',
            name='identificacion',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='credencial',
        ),
        migrations.AddField(
            model_name='anfitrion',
            name='celular',
            field=models.CharField(default='5500000000', max_length=10),
        ),
        migrations.AddField(
            model_name='anfitrion',
            name='contraseña',
            field=models.CharField(default='12345678', max_length=100),
        ),
        migrations.AddField(
            model_name='anfitrion',
            name='correo',
            field=models.EmailField(default='anfitrion@gmail.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='anfitrion',
            name='nombre',
            field=models.CharField(default='Anfitrion', max_length=100),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='celular',
            field=models.CharField(default='5500000000', max_length=15),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='contraseña',
            field=models.CharField(default='12345678', max_length=100),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='correo',
            field=models.EmailField(default='estudiante@gmail.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(default='Estudiante', max_length=100),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='presupuesto',
            field=models.DecimalField(decimal_places=2, default='2000.00', max_digits=10),
        ),
        migrations.AlterField(
            model_name='anfitrion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=255)),
                ('anfitrion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viviendas', to='usuarios.anfitrion')),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
