# Generated by Django 3.2 on 2021-07-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=None, max_length=12),
        ),
    ]
