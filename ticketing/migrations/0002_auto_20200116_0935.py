# Generated by Django 2.2.5 on 2020-01-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printers',
            name='printer',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='PrinterList',
        ),
    ]
