# Generated by Django 4.0 on 2021-12-19 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_bounty_created_on_alter_invoice_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 19, 17, 58, 56, 131363), editable=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 19, 17, 58, 56, 131363), editable=False),
        ),
    ]
