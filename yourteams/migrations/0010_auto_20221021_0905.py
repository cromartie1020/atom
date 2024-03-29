# Generated by Django 3.2.3 on 2022-10-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourteams', '0009_winnerpick_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winnerpick',
            name='actual_winner',
            field=models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Buffalo Bills', 'Buffalo Bills'), ('Chicago Bears', 'Chicago Bears'), ('Carolina Panthers', 'Carolina Panthers'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Denver Broncos', 'Denver Broncos'), ('Detroit lions', 'Detroit lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Jacksonville Jaguars', 'Jacksonvile Jaguars'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Miami Dolphins', 'Miami Dolphins'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New England Patriots', 'New England Patriots'), ('New York Giants', 'New York Giants'), ('New York Jets', 'New York Jets'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seatle Seahawks', 'Seatle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Tennessee Titans', 'Tennessee Titans'), ('Washington Commanders', 'Washington Commanders')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='winnerpick',
            name='away',
            field=models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Buffalo Bills', 'Buffalo Bills'), ('Chicago Bears', 'Chicago Bears'), ('Carolina Panthers', 'Carolina Panthers'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Denver Broncos', 'Denver Broncos'), ('Detroit lions', 'Detroit lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Jacksonville Jaguars', 'Jacksonvile Jaguars'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Miami Dolphins', 'Miami Dolphins'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New England Patriots', 'New England Patriots'), ('New York Giants', 'New York Giants'), ('New York Jets', 'New York Jets'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seatle Seahawks', 'Seatle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Tennessee Titans', 'Tennessee Titans'), ('Washington Commanders', 'Washington Commanders')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='winnerpick',
            name='home',
            field=models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Buffalo Bills', 'Buffalo Bills'), ('Chicago Bears', 'Chicago Bears'), ('Carolina Panthers', 'Carolina Panthers'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Denver Broncos', 'Denver Broncos'), ('Detroit lions', 'Detroit lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Jacksonville Jaguars', 'Jacksonvile Jaguars'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Miami Dolphins', 'Miami Dolphins'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New England Patriots', 'New England Patriots'), ('New York Giants', 'New York Giants'), ('New York Jets', 'New York Jets'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seatle Seahawks', 'Seatle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Tennessee Titans', 'Tennessee Titans'), ('Washington Commanders', 'Washington Commanders')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='winnerpick',
            name='selected_pick',
            field=models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Buffalo Bills', 'Buffalo Bills'), ('Chicago Bears', 'Chicago Bears'), ('Carolina Panthers', 'Carolina Panthers'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Denver Broncos', 'Denver Broncos'), ('Detroit lions', 'Detroit lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Jacksonville Jaguars', 'Jacksonvile Jaguars'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Miami Dolphins', 'Miami Dolphins'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New England Patriots', 'New England Patriots'), ('New York Giants', 'New York Giants'), ('New York Jets', 'New York Jets'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seatle Seahawks', 'Seatle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Tennessee Titans', 'Tennessee Titans'), ('Washington Commanders', 'Washington Commanders')], max_length=250, null=True),
        ),
    ]
