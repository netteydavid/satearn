# Generated by Django 4.0 on 2021-12-27 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_application_created_on_alter_bounty_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 15, 50, 59, 680107), editable=False),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 15, 50, 59, 679107), editable=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 15, 50, 59, 680107), editable=False),
        ),
    ]