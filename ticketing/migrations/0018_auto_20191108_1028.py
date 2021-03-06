# Generated by Django 2.2.5 on 2019-11-08 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0017_ticket_days_opened'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='days_opened',
            field=models.TextField(blank=True, null=True, verbose_name='Days Open'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Body')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketing.Ticket')),
            ],
        ),
    ]
