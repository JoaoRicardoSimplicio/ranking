# Generated by Django 3.0.7 on 2020-06-23 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0002_auto_20200620_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nflinstagrams',
            name='id',
        ),
        migrations.AlterField(
            model_name='nflinstagrams',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='nfl.nflTeams'),
        ),
    ]
