# Generated by Django 4.1.2 on 2022-10-24 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
