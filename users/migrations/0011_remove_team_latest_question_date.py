# Generated by Django 3.2.5 on 2022-01-22 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_team_latest_question_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='latest_question_date',
        ),
    ]
