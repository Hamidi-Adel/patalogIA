# Generated by Django 4.1.2 on 2022-11-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_name_user_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
