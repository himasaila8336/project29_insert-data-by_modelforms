from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage 
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['name']
        #widgets={'url':forms.PasswordInput,'name':forms.Textarea()}
        #labels={'topic_name':'TN','name':'N'}
        help_texts={'topic_name':'should not be integer','name':'alphabets'}
class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord 
        fields='__all__'


