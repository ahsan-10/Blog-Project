# Generated by Django 3.0.3 on 2020-07-30 16:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200730_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 16, 53, 40, 941030, tzinfo=utc)),
        ),
    ]
