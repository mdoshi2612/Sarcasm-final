# Generated by Django 2.2 on 2022-01-15 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader_name', models.CharField(max_length=100)),
                ('leader_roll_number', models.CharField(max_length=100)),
                ('year_of_study', models.CharField(max_length=100)),
                ('team_name', models.CharField(max_length=100)),
                ('team_logo', models.CharField(max_length=100)),
                ('player1', models.CharField(max_length=100)),
                ('player2', models.CharField(max_length=100)),
                ('player3', models.CharField(max_length=100)),
                ('player4', models.CharField(max_length=100)),
            ],
        ),
    ]
