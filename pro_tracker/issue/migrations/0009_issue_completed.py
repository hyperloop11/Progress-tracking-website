# Generated by Django 3.1.1 on 2020-10-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0008_auto_20201023_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]