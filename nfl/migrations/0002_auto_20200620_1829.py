# Generated by Django 3.0.7 on 2020-06-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nflteams',
            name='nfl_profile_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='nflteams',
            name='instagram_link',
            field=models.URLField(null=True),
        ),
    ]
