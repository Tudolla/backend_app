# Generated by Django 5.0.7 on 2024-09-11 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_memberactivity'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='memberactivity',
            table='story_user_tracking',
        ),
    ]
