# Generated by Django 5.1.2 on 2024-10-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencialivro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='ano',
            field=models.IntegerField(),
        ),
    ]
