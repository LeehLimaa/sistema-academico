# Generated by Django 4.2.5 on 2023-09-27 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_tipo_avaliacao_nome_tipo_avaliacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipo_avaliacao',
            old_name='nome_tipo_avaliacao',
            new_name='tipo_avaliacao',
        ),
    ]
