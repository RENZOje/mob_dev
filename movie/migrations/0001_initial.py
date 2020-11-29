# Generated by Django 3.1.3 on 2020-11-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('year', models.IntegerField(default=2020)),
                ('imdbID', models.CharField(max_length=10)),
                ('poster', models.ImageField(upload_to='')),
                ('rated', models.CharField(max_length=10)),
                ('released', models.DateField()),
                ('runtime', models.IntegerField()),
                ('genre', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=200)),
                ('actors', models.CharField(max_length=200)),
                ('plot', models.TextField(max_length=200)),
                ('language', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('awards', models.CharField(max_length=200)),
                ('imdbRating', models.FloatField()),
                ('imdbVotes', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('production', models.CharField(max_length=200)),
            ],
        ),
    ]