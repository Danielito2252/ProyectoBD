# Generated by Django 5.1.1 on 2024-10-23 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_subcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoria',
            name='descripcion',
            field=models.CharField(help_text='Descripcion de la SubCategoria', max_length=100),
        ),
    ]
