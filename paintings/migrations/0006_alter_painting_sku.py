# Generated by Django 3.2.25 on 2024-07-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0005_alter_painting_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='sku',
            field=models.CharField(default='5174a3b2', max_length=8, unique=True),
        ),
    ]
