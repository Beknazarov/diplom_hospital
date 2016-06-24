# -*- coding:utf-8
from django import forms
from medicalhistory.models import (HistoryPatientLife ,
                                   Women)





class HistoryPatientModelForm(forms.ModelForm):
    class Meta:
        model = HistoryPatientLife
        exclude = []
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']=''
            self.fields[field].widget.attrs['style'] = 'width:70%'

class WomenModelForm(forms.ModelForm):

    class Meta:
        model = Women
        exclude = []





