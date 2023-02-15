from django.db import models
import uuid

class demarcate(models.Model):
    idmarks = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)
    right = models.IntegerField(blank=True, null=True)
    bottom = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    idimage = models.ForeignKey('images.Image', models.DO_NOTHING, db_column='idimagem', blank=True, null=True)

    class Meta:
        db_table = 'demarcate'

class demarcateQuestion(models.Model):
    idmarks = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    questionImage = models.ImageField(upload_to='question_images/', null=True, blank=True)
    question = models.CharField(max_length=500)
    questionMarks = models.CharField(max_length=100, default='5.0')
    

    def __str__(self):
        return self.question