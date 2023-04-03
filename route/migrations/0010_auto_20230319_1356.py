# Generated by Django 3.2.5 on 2023-03-19 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0009_ais_data_updates'),
    ]

    operations = [
        migrations.AddField(
            model_name='ais_data_report',
            name='destination',
            field=models.CharField(blank=True, max_length=111, null=True),
        ),
        migrations.AddField(
            model_name='ais_data_report',
            name='source',
            field=models.CharField(blank=True, max_length=111, null=True),
        ),
        migrations.AddField(
            model_name='ais_data_report',
            name='type_of_item',
            field=models.CharField(blank=True, max_length=111, null=True),
        ),
    ]
