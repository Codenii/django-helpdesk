# Generated by Django 2.2.5 on 2019-11-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0019_auto_20191108_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Private Comment'),
            preserve_default=False,
        ),
    ]