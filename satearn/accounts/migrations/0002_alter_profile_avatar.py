# Generated by Django 4.0 on 2021-12-28 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='registration/default_pic.jpg', upload_to=''),
        ),
    ]
