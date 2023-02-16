from django.db import models
import uuid

# Demarcte Questions or MCQS!
class QuestionTypes(models.Model):
    idtype_questions = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    category = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'question_types'

    def __str__(self):
        return self.category

class Questions(models.Model):
    idquestions = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    question = models.IntegerField(db_column='questaoNum', blank=True, null=True)  # Field name made lowercase.z    
    description = models.CharField(max_length=150, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    certain = models.CharField(max_length=1, blank=True, null=True, default="A")
    typequestionandidtypequestion = models.ForeignKey('QuestionTypes', models.DO_NOTHING, verbose_name="Type of Question", db_column='tipoquestoesidtipoquestoes', blank=True, null=True)
    questionnaireidquestionnaire = models.ForeignKey('Questionnaire', models.DO_NOTHING, verbose_name="Related Subject", db_column='questionarioidquestionario', blank=True, null=True)
    videoidvideo = models.ForeignKey('video.Video', models.DO_NOTHING, verbose_name="Link Video", db_column='videoidvideo', blank=True, null=True)
    codimage = models.ForeignKey('images.Image', models.DO_NOTHING, verbose_name="Link Image", db_column='codimagem', blank=True, null=True)

    class Meta:
        db_table = 'questions'
    
    def __str__(self):
        return self.description


class Questionnaire(models.Model):
    idquestionnaire = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=150, blank=True, null=True)
    Subject = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    quests = models.IntegerField(blank=True, null=True)
    #Co Educator This Feild needs to be addressed
    co_educator = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='codidusuario', blank=True, null=True)
    usercode = models.ForeignKey('accounts.UserType', models.DO_NOTHING, db_column='codtipousuario', blank=True, null=True)

    class Meta:
        db_table = 'questionnaire'
    def __str__(self):
        return self.Subject

#MCQS Option
class AlternativeQuestions(models.Model):
    idquestions_alternatives = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    description = models.CharField(max_length=250, blank=True, null=True)
    letter = models.CharField(max_length=1, blank=True, null=True)
    questoes_questoes_id = models.ForeignKey('Questions', models.DO_NOTHING, verbose_name="Related Question", db_column='questoes_idquestoes')

    class Meta:
        db_table = 'alternative_questions'
    def __str__(self):
        return self.description



class Result(models.Model):
    idresult = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    iduser_user = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='usuario_idusuario', blank=True, null=True)
    quiz_quiz_id = models.ForeignKey('Questionnaire', models.DO_NOTHING, db_column='questionario_idquestionario', blank=True, null=True)
    descriptiondate = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'result'


# Temp
class Cases(models.Model):
    idcase = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    imageidimage = models.ForeignKey('images.Image', models.DO_NOTHING, db_column='imagemidimagem', blank=True, null=True)
    # This Needs to be Discussed
    this_question = models.ForeignKey('Questions', models.DO_NOTHING, db_column='questoesidquestao')
    useriduser = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='usuarioidusuario', blank=True, null=True)

    class Meta:
        db_table = 'cases'


class QuestionWiseResult(models.Model):
    idQuestionResult = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    questionLink = models.ForeignKey('demarcate.demarcateQuestion', on_delete=models.DO_NOTHING)
    marksObtain = models.CharField(max_length=100, default= '0')


class SubjectWiseResult(models.Model):
    idResult = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    subjectName = models.CharField(max_length=500, blank=True, null= True)
    studentInfo = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    marksObtain = models.CharField(max_length=100, default= '0')

class CompleteResult(models.Model):
    idCompleteResult = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    studentInfo = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    totalObtainedMarks = models.CharField(max_length=100, default= '0')



class questionsWithImages(models.Model):
    idQuestion = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    questionImage = models.ImageField(upload_to='question_images/', null=True, blank=True)
    questionDescription = models.CharField(max_length=1000, null=True, blank=True)
    questionOptionA = models.CharField(max_length=2, null=True, blank=True)
    quetionOptionADescription = models.CharField(max_length=500, null=True, blank=True)
    questionOptionB = models.CharField(max_length=2, null=True, blank=True)
    quetionOptionBDescription = models.CharField(max_length=500, null=True, blank=True)
    questionOptionC = models.CharField(max_length=2, null=True, blank=True)
    quetionOptionCDescription = models.CharField(max_length=500, null=True, blank=True)
    questionOptionD = models.CharField(max_length=2, null=True, blank=True)
    quetionOptionDDescription = models.CharField(max_length=500, null=True, blank=True)
    rightAnswerOfQuestion = models.CharField(max_length=2, null=True, blank=True, default="A")
    def __str__(self):
        return self.questionDescription

class questionsWithOutImages(models.Model):
    idQuestion = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    questionDescription = models.CharField(max_length=1000, null=True, blank=True)
    questionOptionA = models.CharField(max_length=2, null=True, blank=True)
    quetionOptionADescription = models.CharField(max_length=500, null=True, blank=True)
    questionOptionB = models.CharField(max_length=2, null=True, blank=True)
    quetionOptionBDescription = models.CharField(max_length=500, null=True, blank=True)
    questionOptionC = models.CharField(max_length=2, null=True, blank=True)
    quetionOptionCDescription = models.CharField(max_length=500, null=True, blank=True)
    questionOptionD = models.CharField(max_length=2, null=True, blank=True)
    quetionOptionDDescription = models.CharField(max_length=500, null=True, blank=True)
    rightAnswerOfQuestion = models.CharField(max_length=2, null=True, blank=True, default="A")
    def __str__(self):
        return self.questionDescription