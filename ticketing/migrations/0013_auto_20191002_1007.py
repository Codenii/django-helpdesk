# Generated by Django 2.2.5 on 2019-10-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ticketing", "0012_auto_20190930_1030")]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="u_sort_type",
            field=models.CharField(
                blank=True,
                default="-pk",
                max_length=30,
                null=True,
                verbose_name="Sort By Value",
            ),
        )
    ]
