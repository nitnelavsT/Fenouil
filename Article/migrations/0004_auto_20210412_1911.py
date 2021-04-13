# Generated by Django 3.1.7 on 2021-04-12 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_auto_20210329_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'cartegorie',
                'verbose_name_plural': 'cartegories',
                'ordering': ('nom',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='nom_article',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='article',
            name='quantite_article',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterIndexTogether(
            name='article',
            index_together={('id', 'slug')},
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Article', to='Article.categorie'),
        ),
    ]