from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import connection
from django.db.models import F

from shop.models import *
from captcha.fields import CaptchaField, CaptchaTextInput

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

from django.forms import ModelChoiceField


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "".join(list(obj.values()))


class AddToCarz(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AddToCarz, self).__init__(*args, **kwargs)

        self.fields['color'] = ModelChoiceField(queryset=ColorProduct.objects.filter(women__pk=args[-1].get('pk_t')))
        self.fields['size'] = ModelChoiceField(queryset=SizeProduct.objects.filter(women__pk=args[-1].get('pk_t')))

    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)

    class Meta:
        model = Women
        fields = ('color', 'size')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'registration__form_input', 'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'registration__form_input', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'registration__form_input', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'registration__form_input', 'placeholder': 'Повтор пароля'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'registration__form_input', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'registration__form_input', 'placeholder': 'Пароль'}))
