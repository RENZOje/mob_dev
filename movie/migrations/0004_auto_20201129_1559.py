# Generated by Django 3.1.3 on 2020-11-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20201129_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdbVotes',
            field=models.CharField(max_length=20),
        ),
    ]