# Generated by Django 4.1.2 on 2022-11-21 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('idreport', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('report', models.CharField(blank=True, max_length=2000, null=True)),
                ('idimage', models.ForeignKey(blank=True, db_column='idimagem', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='images.image')),
                ('iduser', models.ForeignKey(blank=True, db_column='idusuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'report',
            },
        ),
    ]