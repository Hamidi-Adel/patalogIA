from django.contrib import admin
from .models import Questions,AlternativeQuestions,QuestionTypes,Questionnaire,Result,Cases,QuestionWiseResult,SubjectWiseResult,CompleteResult,questionsWithImages,questionsWithOutImages

admin.site.register(Questions)
admin.site.register(AlternativeQuestions)
admin.site.register(QuestionTypes)
admin.site.register(Questionnaire)
admin.site.register(Result)
admin.site.register(Cases)
admin.site.register(QuestionWiseResult)
admin.site.register(SubjectWiseResult)
admin.site.register(CompleteResult)
admin.site.register(questionsWithImages)
admin.site.register(questionsWithOutImages)