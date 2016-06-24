# coding: utf-8
from django import forms


class CouponField(forms.CharField):
    def to_python(self, value):
        return value.lower()


class LoginForm(forms.Form):
    login = CouponField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = CouponField(widget=forms.TextInput(attrs={'placeholder': 'Пароль', 'type': 'password'}),
                           max_length=100)


class PasswordChangeForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Введите ваш email'}))
