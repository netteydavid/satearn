# Generated by Django 4.0 on 2022-01-16 16:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0012_alter_application_created_on_alter_bounty_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 10, 10, 29, 674393), editable=False),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignments', related_query_name='assignment', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='completed_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 10, 10, 29, 673392), editable=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 10, 10, 29, 673392), editable=False),
        ),
    ]