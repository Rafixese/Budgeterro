# Generated by Django 4.1 on 2023-02-11 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_budgetobj_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgetobj',
            options={'permissions': [('can_manage_budgetobj', 'Can manage budget objects')]},
        ),
    ]