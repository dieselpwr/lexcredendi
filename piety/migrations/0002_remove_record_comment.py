# Generated by Django 3.0 on 2019-12-11 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piety', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='comment',
        ),
    ]
