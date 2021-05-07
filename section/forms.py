from django import forms
from django.utils.translation import gettext_lazy
from .models import UserProfile, Anketa, Comment, Apeal
from django.contrib.auth.forms import UserCreationForm



class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ('image', 'first_name', 'last_name', 'username', 'email')
        labels = {
            'image': gettext_lazy('Изображение')
        }


class UpdateProfile(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ('image', 'first_name', 'last_name', 'email')
        labels = {
            'image': gettext_lazy('Изображение')
        }


class AnketaForm(forms.ModelForm):
    class Meta:
        model = Anketa
        fields = ('title', 'types', 'descriptions', 'time_plan', 'phone', 'age', 'price', 'sity', 'image')
        labels = {
            'title': gettext_lazy('Название'),
            'types': gettext_lazy('Вид'),
            'descriptions': gettext_lazy('Описание'),
            'time_plan': gettext_lazy('Расписание занятий'),
            'phone': gettext_lazy('Телефон'),
            'age': gettext_lazy('Возраст'),
            'price': gettext_lazy('Цена'),
            'sity': gettext_lazy('Район'),
            'image': gettext_lazy('Изображение'),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class ApealForm(forms.ModelForm):
    class Meta:
        model = Apeal
        fields = ('types', 'text', )


dict1 = (
    ('S', 'Секция'),
    ('M', 'Мероприятие'),
)

dict2 = (
    ('K', 'Кировский'),
    ('L', 'Ленинский'),
    ('O', 'Октябрьский'),
    ('Sv', 'Свердловский'),
    ('S', 'Советский'),
    ('Z', 'Центральный'),
)


class AnketaFilterForm(forms.Form):
    blank_choice = (('', '--- Выберите значение ---'),) 
    min_price = forms.IntegerField(label='цена от:', required=False)
    max_price = forms.IntegerField(label='цена до:', required=False)
    min_age = forms.IntegerField(label='возраст от:', required=False)
    max_age = forms.IntegerField(label='возраст до:', required=False)
    types = forms.ChoiceField(label='Тип:', choices=blank_choice + dict1, required=False)
    sity = forms.ChoiceField(label='Район:', choices=blank_choice + dict2, required=False)