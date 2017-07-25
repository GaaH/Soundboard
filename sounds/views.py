from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from.models import Sound, Soundbox


class IndexView(ListView):
    template_name = 'sounds/index.html'
    queryset = Sound.objects.order_by('-created_at')[:20]


class SoundDetailView(DetailView):
    model = Sound

class SoundboxDetailView(DetailView):
    model = Soundbox

@method_decorator(login_required, name='dispatch')
class NewSoundView(CreateView):
    model = Sound
    fields = ['title', 'file', 'description']

    def form_valid(self, form):
        # TOOD: Check if the soundbox belongs to the user
        form.instance.soundbox = get_object_or_404(Soundbox, pk=self.kwargs['pk'], user=self.request.user)
        return super(NewSoundView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NewSoundView, self).get_context_data(**kwargs)
        context['soundbox'] = self.kwargs['pk']
        return context

@method_decorator(login_required, name='dispatch')
class NewSoundboxView(CreateView):
    model = Soundbox
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewSoundboxView, self).form_valid(form)
