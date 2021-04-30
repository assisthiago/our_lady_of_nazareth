# Generated by Django 3.1.6 on 2021-04-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysteries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystery',
            name='sequence',
            field=models.CharField(choices=[(1, 'Primeiro mistério'), (2, 'Segundo mistério'), (3, 'Terceiro mistério'), (4, 'Quarto mistério'), (5, 'Quinto mistério')], max_length=50, verbose_name='Ordem da sequência'),
        ),
    ]
