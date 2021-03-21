# Generated by Django 3.1.7 on 2021-03-21 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_article', models.IntegerField()),
                ('nom_article', models.CharField(max_length=100)),
                ('quantite_article', models.IntegerField(default=0)),
                ('commande', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='Client.commande')),
            ],
        ),
    ]
