# Generated by Django 5.0.7 on 2024-08-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0023_alter_painting_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='sku',
            field=models.CharField(default='951573f5', max_length=8, unique=True),
        ),
    ]
