# Generated by Django 2.2.5 on 2022-01-18 12:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220118_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='current_level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Level'),
        ),
        migrations.AddField(
            model_name='team',
            name='current_level_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
