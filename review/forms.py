from django import forms
from .models import Feedback

# class FeedbackForm(forms.Form):
#     realm = forms.CharField(label='Область искусства:')
#     name = forms.CharField(label='Фамилия Имя:',error_messages={'required':'Это поле должно быть не пустым'})
#     rating = forms.IntegerField(label='Ваша оценка:', max_value=5, min_value=1)
#     feedback = forms.CharField(label='Ваш отзыв:',widget=forms.Textarea(attrs={'rows':2,'cols':20}))


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'realm':'Область искусства:',
            'name':'Фамилия Имя:',
            'rating':'Ваша оценка:',
            'feedback':'Ваш отзыв:'

        }
        error_messages = {
            'name':{
                'max_lenght':'Слишком большая длина',
                'min_lenght':'Слишком маленькая длина',
                'required':'Это поле не должно быть пустым'
            },
           'realm': {
               'max_lenght': 'Слишком большая длина',
               'min_lenght': 'Слишком маленькая длина',
               'required': 'Это поле не должно быть пустым'
            }
        }
