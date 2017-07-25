from django.conf.urls import url
from .views import SoundDetailView, IndexView, NewSoundView, NewSoundboxView, SoundboxDetailView

app_name = 'sounds'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', SoundDetailView.as_view(), name='detail'),
    url(r'^soundbox/(?P<pk>\d+)/new/$', NewSoundView.as_view(), name='new'),

    url(r'^soundbox/(?P<pk>\d+)/$', SoundboxDetailView.as_view(), name='detail-box'),
    url(r'^soundbox/new/$', NewSoundboxView.as_view(), name='new-box'),
]
