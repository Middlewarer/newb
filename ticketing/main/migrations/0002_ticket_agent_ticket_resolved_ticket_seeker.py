# Generated by Django 5.0.4 on 2024-05-01 18:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='agent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tickets_as_seeker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='seeker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tickets_as_agent', to=settings.AUTH_USER_MODEL),
        ),
    ]
