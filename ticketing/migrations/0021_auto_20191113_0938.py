# Generated by Django 2.2.5 on 2019-11-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0020_comment_is_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Private Comment'),
        ),
    ]
