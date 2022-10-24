# Generated by Django 4.1.2 on 2022-10-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('idvideo', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'video',
                'managed': False,
            },
        ),
    ]
