from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^home/$', home, name='home'),
    url(r'^sobre/$', about, name='about'),
    url(r'^equipe/$', team, name='team'),
    url(r'^contato/$', contact, name='contact'),
    url(r'^apoio/', supporters, name='supporters'),
    url(r'^cursos/', courses, name='courses'),
    url(r'^processo/(?P<year>\d{4})(?:/(?P<half>\d{1}))?/', sprocess, name='sprocess'),
]
