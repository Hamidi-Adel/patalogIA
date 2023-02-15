# Generated by Django 4.1.2 on 2023-02-12 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0003_remove_alternativequestions_certain_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectWiseResult',
            fields=[
                ('idResult', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('subjectName', models.CharField(blank=True, max_length=500, null=True)),
                ('marksObtain', models.CharField(blank=True, max_length=100, null=True)),
                ('studentInfo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompleteResult',
            fields=[
                ('idCompleteResult', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('totalObtainedMarks', models.CharField(blank=True, max_length=100, null=True)),
                ('studentInfo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
