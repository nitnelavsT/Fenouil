# Generated by Django 3.1.7 on 2021-03-30 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_auto_20210329_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='Commande_article',
        ),
    ]