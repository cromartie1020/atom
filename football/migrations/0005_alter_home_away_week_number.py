# Generated by Django 3.2.3 on 2021-07-15 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0004_auto_20210714_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_away',
            name='week_number',
            field=models.IntegerField(default=1),
        ),
    ]