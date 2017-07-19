from django.conf.urls import url
from .views import SoundDetailView, IndexView, NewSoundView

app_name = 'sounds'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', SoundDetailView.as_view(), name='detail'),
    url(r'^new/$', NewSoundView.as_view(), name='new'),
]
