# Generated by Django 2.2.5 on 2019-11-08 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0018_auto_20191108_1028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
