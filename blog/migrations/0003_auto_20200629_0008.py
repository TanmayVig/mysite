# Generated by Django 3.0.7 on 2020-06-28 18:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200628_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creat_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 18, 38, 59, 838894, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='creat_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 18, 38, 59, 838894, tzinfo=utc)),
        ),
    ]