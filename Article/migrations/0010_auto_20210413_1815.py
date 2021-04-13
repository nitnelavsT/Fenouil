# Generated by Django 3.1.7 on 2021-04-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0009_auto_20210413_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='nom_article',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='article',
            name='quantite_article',
            field=models.IntegerField(default=0),
        ),
    ]