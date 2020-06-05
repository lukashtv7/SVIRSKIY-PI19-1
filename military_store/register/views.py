from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import RegisterForm
from django.http import HttpResponseRedirect


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'register/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})
