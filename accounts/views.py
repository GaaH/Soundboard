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

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is None:
            if self.request.user.is_authenticated():
                self.kwargs[self.pk_url_kwarg] = self.request.user.pk
            else:
                return None

        return super(ProfileView, self).get_object(queryset=None)

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object is None:
            return redirect(reverse('accounts:login'))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
