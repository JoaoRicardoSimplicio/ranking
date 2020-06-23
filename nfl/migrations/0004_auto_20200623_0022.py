# Generated by Django 3.0.7 on 2020-06-23 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0003_auto_20200623_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='nflinstagrams',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nflinstagrams',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfl.nflTeams'),
        ),
    ]
