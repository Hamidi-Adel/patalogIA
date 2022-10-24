# Generated by Django 4.1.2 on 2022-10-24 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0002_alter_video_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='co_educator',
            field=models.ForeignKey(blank=True, db_column='codidusuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
