# Generated by Django 3.1.4 on 2021-01-30 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('khalidblog_app', '0004_auto_20210129_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentreply',
            name='name',
        ),
    ]
