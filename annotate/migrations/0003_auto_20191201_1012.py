# Generated by Django 2.2.7 on 2019-12-01 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('annotate', '0002_annotation_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='reviewed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]