# Generated by Django 3.0.2 on 2020-03-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0007_newstaff_ns_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='tr_body',
            field=models.TextField(blank=True, null=True, verbose_name='Additional Information (If Any)'),
        ),
    ]
