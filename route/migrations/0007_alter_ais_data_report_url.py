# Generated by Django 3.2.5 on 2023-02-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0006_ais_data_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ais_data_report',
            name='URL',
            field=models.TextField(),
        ),
    ]
