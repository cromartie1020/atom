# Generated by Django 3.2.3 on 2022-10-21 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0015_auto_20221021_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_away',
            name='week_number',
            field=models.IntegerField(default=6),
        ),
    ]
