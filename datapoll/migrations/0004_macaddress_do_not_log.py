# Generated by Django 3.1 on 2020-08-25 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapoll', '0003_auto_20200822_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='macaddress',
            name='do_not_log',
            field=models.BooleanField(default=False),
        ),
    ]