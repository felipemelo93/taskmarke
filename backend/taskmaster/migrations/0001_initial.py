# Generated by Django 5.1.1 on 2024-10-08 16:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField()),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('E', 'En progreso'), ('C', 'Completado')], default='P', max_length=1)),
                ('prioridad', models.CharField(choices=[('B', 'Baja'), ('M', 'Media'), ('A', 'Alta')], default='M', max_length=1)),
                ('etiquetas', models.ManyToManyField(blank=True, to='taskmaster.etiqueta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
