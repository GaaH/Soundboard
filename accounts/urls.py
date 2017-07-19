from django.conf.urls import include, url
from .views import SignupView, ProfileView

app_name = 'accounts'
urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^profile/$', ProfileView.as_view(), name='profile-connected'),
    url(r'^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name='profile'),
    url(r'^', include('django.contrib.auth.urls'))
]
