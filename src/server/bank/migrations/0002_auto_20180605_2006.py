# Generated by Django 2.0.6 on 2018-06-05 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='uploadedby',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='problem-setter'),
        ),
    ]
