from django import forms
from dz_v1 import models

class RegistrationForm(forms.Form):
    login = forms.CharField(min_length=5, label='Логин')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторный ввод пароля')
    email = forms.EmailField()
    surname = forms.CharField(label='Фамилия')
    name = forms.CharField(label='Имя')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'id':'inputEmail'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        p = cleaned_data.get("password")
        p2 = cleaned_data.get("password2")
        l = cleaned_data.get("login")
        model = models.UserModel.objects.values('login')
        if p and p2 and l:
            # Only do something if both fields are valid so far.
            if p != p2:
                raise forms.ValidationError("Пароли не совпадают")
            #elif model.count(l) != 0:
               # raise forms.ValidationError("Такой логин уже существует")