# Generated by Django 4.1.2 on 2023-02-16 13:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('idimage', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('path', models.CharField(blank=True, max_length=250, null=True)),
                ('question_image', models.ImageField(blank=True, null=True, upload_to='question_images/')),
                ('dataimg', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='ImageType',
            fields=[
                ('id_type_image', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'image_type',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('idespecialty', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'specialty',
            },
        ),
        migrations.CreateModel(
            name='ImagesQuestions',
            fields=[
                ('idimages_questions', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('daterecord', models.DateTimeField(blank=True, null=True)),
                ('id_image', models.ForeignKey(blank=True, db_column='id_imagem', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='images.image')),
            ],
            options={
                'db_table': 'images_questions',
            },
        ),
    ]
