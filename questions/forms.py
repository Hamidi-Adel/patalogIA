from images.models import Image
from video.models import Video
from .models import QuestionTypes,Questions,Questionnaire, AlternativeQuestions
from django import forms
from demarcate.models import demarcateQuestion




class QuestionTypeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=QuestionTypes.objects.all(), to_field_name="category", empty_label="Select Category", label='')
    category.widget.attrs.update({'class': 'form-select', 'placeholder': 'category'})
    class Meta:
        model = QuestionTypes
        fields = '__all__'


class CreateQuestionsForm(forms.ModelForm):
    question = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Question'}), label='')
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}), label='')
    value = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Value'}), label='')
    certain = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Certain'}), label='')
    questionnaireidquestionnaire = forms.ModelChoiceField(
        queryset=Questionnaire.objects.all(),
        label="",
        empty_label="Select questionnaireidquestionnaire"
    )
    questionnaireidquestionnaire.widget.attrs.update({'class': 'form-select', 'placeholder': 'Video Link'})
    class Meta:
        model = Questions
        fields = '__all__'
        exclude = ['typequestionandidtypequestion','videoidvideo','codimage']
        

class CreateQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = '__all__'
        exclude = ['videoidvideo','codimage']


class CreateOptionsforAQuestion(forms.ModelForm):
    
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Option Description (e.g. 14 Feb 2023)'}), label='')
    letter = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Optiion Letter (e.g. A,B,C or D)'}), label='')
    questoes_questoes_id = forms.ModelChoiceField(
        queryset=Questions.objects.all(),
        label="",
        empty_label="Select A Question")
    class Meta:
        model = AlternativeQuestions
        fields = '__all__'


class createImageQuestion(forms.ModelForm):
    question = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Question'}), label='')
    questionImage = forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'question', 'name':"question_image", 'id':'id_questionImage'})
    class Meta:
        model = demarcateQuestion 
        fields = '__all__'
        exclude = ('x','y','w','h','area','questionMarks')
