# Generated by Django 3.2.3 on 2022-09-26 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yourteams', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='winnerpick',
            old_name='winner',
            new_name='winningPicks',
        ),
    ]
