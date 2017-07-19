from django.shortcuts import redirect, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupView(generic.FormView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = '/sounds/1'

    def form_valid(self, form):
        form.save()
        return redirect('sounds:detail', pk=1)


class ProfileView(generic.DetailView):
    model = User
