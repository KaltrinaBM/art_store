# Generated by Django 5.0.7 on 2024-08-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0022_alter_painting_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='sku',
            field=models.CharField(default='fc4a70dc', max_length=8, unique=True),
        ),
    ]
