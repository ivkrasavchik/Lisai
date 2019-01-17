import unicodedata

from django import forms
from django.core import validators
from django.forms import Textarea, TextInput, NumberInput, CharField, EmailInput

from .models import Zvonki, Questions


class ZvonkiForm(forms.ModelForm):

    class Meta:
        model = Zvonki
        fields = ("verbose_name", "phone", "category", "short_description")
        # widgets = {
        #            'short_description': Textarea(attrs={
        #                 'placeholder': "Краткое описание", 'id': "short_description_z"
        #            }),
        #            'verbose_name': TextInput(attrs={
        #                'placeholder': "Ваше имя", 'id': "verbose_name_z"
        #            })
        # }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class UsernameFieldEmail(CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))

    widget = EmailInput(attrs={
            'autofocus': True,
            'style': 'margin: 0.5vw; padding:1vw;height:3vh;',
            'class': 'form-control col-sm-12',
            'placeholder': 'Введите Ваш Email'
        })
    default_validators = [validators.EmailValidator(message='Email то липовый')]

    def __init__(self, **kwargs):
        super().__init__(strip=True, **kwargs)


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ("verbose_name", "category", "short_description", "email")
        field_classes = {'email': UsernameFieldEmail}

        # widgets = {
        #            'short_description': Textarea(attrs={
        #                 'placeholder': "Краткое описание", 'id': "short_description_z"
        #            }),
        #            'verbose_name': TextInput(attrs={
        #                'placeholder': "Ваше имя", 'id': "verbose_name_z"
        #            })
        # }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

