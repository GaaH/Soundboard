from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, TemplateView

from.models import Sound


class IndexView(TemplateView):
    template_name = 'sounds/index.html'


class SoundDetailView(DetailView):
    model = Sound


@method_decorator(login_required, name='dispatch')
class NewSoundView(CreateView):
    model = Sound
    fields = ['title', 'file', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewSoundView, self).form_valid(form)
