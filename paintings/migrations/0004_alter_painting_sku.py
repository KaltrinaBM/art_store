# Generated by Django 3.2.25 on 2024-07-25 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0003_auto_20240724_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='sku',
            field=models.CharField(default='aa0a4ece', max_length=8, unique=True),
        ),
    ]