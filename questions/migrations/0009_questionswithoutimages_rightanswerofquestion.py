# Generated by Django 4.1.2 on 2023-02-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_questionswithimages_rightanswerofquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionswithoutimages',
            name='rightAnswerOfQuestion',
            field=models.CharField(blank=True, default='A', max_length=2, null=True),
        ),
    ]