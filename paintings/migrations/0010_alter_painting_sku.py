# Generated by Django 3.2.25 on 2024-08-04 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0009_alter_painting_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='sku',
            field=models.CharField(default='dfe95468', max_length=8, unique=True),
        ),
    ]
