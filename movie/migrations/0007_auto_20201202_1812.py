# Generated by Django 3.1.3 on 2020-12-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_collage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collage',
            name='list_obj',
            field=models.JSONField(default=dict),
        ),
    ]