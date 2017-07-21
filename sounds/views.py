from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from.models import Sound


class IndexView(ListView):
    template_name = 'sounds/index.html'
    queryset = Sound.objects.order_by('-created_at')[:20]


class SoundDetailView(DetailView):
    model = Sound


@method_decorator(login_required, name='dispatch')
class NewSoundView(CreateView):
    model = Sound
    fields = ['title', 'file', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewSoundView, self).form_valid(form)
