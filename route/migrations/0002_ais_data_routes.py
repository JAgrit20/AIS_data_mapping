# Generated by Django 3.2.5 on 2023-02-07 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AIS_data_routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ship_id', models.BigIntegerField()),
                ('Latitude', models.DecimalField(decimal_places=5, max_digits=6)),
                ('Logitude', models.DecimalField(decimal_places=5, max_digits=6)),
            ],
        ),
    ]
