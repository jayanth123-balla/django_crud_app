# Generated by Django 3.0.8 on 2021-03-17 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(default=-1.0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
