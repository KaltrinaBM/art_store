# Generated by Django 3.2.25 on 2024-07-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0004_alter_painting_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='sku',
            field=models.CharField(default='d119d0b4', max_length=8, unique=True),
        ),
    ]