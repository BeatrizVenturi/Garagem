# Generated by Django 5.0.2 on 2024-04-01 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_acessorio"),
    ]

    operations = [
        migrations.RenameField(
            model_name="acessorio",
            old_name="nome",
            new_name="descricao",
        ),
        migrations.RemoveField(
            model_name="acessorio",
            name="site",
        ),
    ]
