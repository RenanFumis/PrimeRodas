# Generated by Django 5.0.7 on 2024-08-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_carinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='summary_car',
            field=models.TextField(blank=True, null=True),
        ),
    ]
