from django import forms
from .models import Feedbacks


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['artist','rating','feedback']
        labels = {
            'artist':'Выберите артиста:',
            'rating':'Ваша оценка:',
            'feedback':'Ваш отзыв:'
        }
        error_messages = {
           'realm': {
               'max_lenght': 'Слишком большая длина',
               'min_lenght': 'Слишком маленькая длина',
               'required': 'Это поле не должно быть пустым'
            }
        }
