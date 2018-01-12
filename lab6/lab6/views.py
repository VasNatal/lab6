from django.shortcuts import render
from django.views.generic import ListView
from dz_v1 import models
from django.views.generic import View
from django.http import HttpResponseRedirect
from dz_v1 import forms
# Create your views here.
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm



class reg_view(ListView):
    model = models.UserModel

    def get(self, request):
        form = forms.RegistrationForm()
        return render(request, 'reg.html', {'form': form})

    def post(self, request):

        if request.method == 'POST':
            form = forms.RegistrationForm(request.POST)
            if form.is_valid():
                login = form.cleaned_data['login']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']
                surname = form.cleaned_data['surname']
                name = form.cleaned_data['name']
                model = models.UserModel(name=name, login=login, password=password, email=email, surname=surname)
                model.save()
                form = forms.RegistrationForm()
        return render(request, 'reg.html', {'form': form})


class book_view(ListView):
    model = models.BookModel

    def get(self, request):
        d = dict(orders=self.model.objects.values('name','author','year', 'description'))
        return render(request, "book.html", d)
