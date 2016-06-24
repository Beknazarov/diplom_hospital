# coding: utf-8
import datetime

from django import forms
from django.forms import TextInput

from KIF.models import Patient


class DateInput(forms.DateInput):
    input_type = 'date'


class PasswordInputType(TextInput):
    input_type = 'password'


class UpdateProfileInfo(forms.ModelForm):
    class Meta:
        model = Patient
        widgets = {
            'password_pat': PasswordInputType(),
            'date_born_pat': DateInput(format='%Y-%m-%d')

        }
        fields = ['surname_pat', 'name_pat', 'last_name_pat', 'date_born_pat', 'email_pat', 'login_pat', 'photo_pat',
                  'password_pat']

    def clean(self):
        cleaned_data = super(UpdateProfileInfo, self).clean()
        data_born = self.cleaned_data.get('date_born_pat')
        if datetime.date(1930, 1, 1) > data_born or data_born > datetime.date.today():
            raise forms.ValidationError('Error')

        return cleaned_data
