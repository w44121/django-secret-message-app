# Generated by Django 3.1.7 on 2021-03-10 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secret_message', '0003_secrtemessage_amount_to_read'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SecrteMessage',
            new_name='SecretMessage',
        ),
    ]
