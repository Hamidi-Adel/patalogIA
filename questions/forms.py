from images.models import Image
from video.models import Video
from .models import QuestionTypes,Questions,Questionnaire
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
    videoidvideo = forms.ModelChoiceField(
        queryset=Video.objects.all(),
        label="",
        empty_label="Select videoidvideo"
    )
    videoidvideo.widget.attrs.update({'class': 'form-select', 'placeholder': 'Video Link'})
    codimage = forms.ModelChoiceField(
        queryset=Image.objects.all(),
        label="",
        empty_label="Select codimage"
    )
    codimage.widget.attrs.update({'class': 'form-select', 'placeholder': 'Video Link'})
    class Meta:
        model = Questions
        fields = '__all__'
        exclude = ['typequestionandidtypequestion']
        

class CreateQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class createImageQuestion(forms.ModelForm):
    question = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Question'}), label='')
    questionImage = forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'question', 'name':"question_image", 'id':'id_questionImage'})
    class Meta:
        model = demarcateQuestion 
        fields = '__all__'
        exclude = ('x','y','w','h','area','questionMarks')
