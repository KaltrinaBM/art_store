# Generated by Django 5.0.7 on 2024-08-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0017_alter_painting_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='sku',
            field=models.CharField(default='3f3ff092', max_length=8, unique=True),
        ),
    ]
