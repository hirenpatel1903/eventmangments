# Generated by Django 3.2.9 on 2022-05-22 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20220518_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='terms_confirmed',
        ),
    ]
