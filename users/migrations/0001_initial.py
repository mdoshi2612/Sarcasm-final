# Generated by Django 4.0.1 on 2022-01-18 14:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('question', models.CharField(blank=True, max_length=1000)),
                ('answer', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static')),
                ('audiofile', models.FileField(blank=True, null=True, upload_to='static/', verbose_name='')),
                ('videofile', models.FileField(blank=True, null=True, upload_to='static/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('leader_name', models.CharField(max_length=100)),
                ('leader_roll_number', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('year_of_study', models.CharField(max_length=100)),
                ('team_name', models.CharField(max_length=100)),
                ('team_logo', models.CharField(max_length=100, null=True)),
                ('player1', models.CharField(max_length=100)),
                ('player2', models.CharField(max_length=100)),
                ('player3', models.CharField(max_length=100)),
                ('player4', models.CharField(max_length=100)),
                ('current_level_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('score', models.IntegerField(default=0)),
                ('current_level', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.level')),
            ],
        ),
    ]
