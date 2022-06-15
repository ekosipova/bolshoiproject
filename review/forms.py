from django import forms

class FeedbackForm(forms.Form):
    realm = forms.CharField(label='Область искусства:')
    name = forms.CharField(label='Фамилия Имя:',error_messages={'required':'Это поле должно быть не пустым'})
    rating = forms.IntegerField(label='Ваша оценка:', max_value=5, min_value=1)
    feedback = forms.CharField(label='Ваш отзыв:',widget=forms.Textarea(attrs={'rows':2,'cols':20}))
