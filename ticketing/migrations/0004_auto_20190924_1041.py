# Generated by Django 2.2.5 on 2019-09-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0003_auto_20190924_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='u_password',
            field=models.CharField(max_length=100, verbose_name='User Password'),
        ),
    ]