# Generated by Django 5.0.7 on 2024-08-11 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0025_alter_painting_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='sku',
            field=models.CharField(default='29a13d2e', max_length=8, unique=True),
        ),
    ]
