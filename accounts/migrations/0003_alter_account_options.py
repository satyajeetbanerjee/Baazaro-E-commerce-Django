# Generated by Django 5.2.1 on 2025-06-03 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_last_login'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Accounts', 'verbose_name_plural': 'Account'},
        ),
    ]
