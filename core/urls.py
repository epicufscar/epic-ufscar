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
    url(r'^processo/2017/1/', sprocess_2017_1, name='sprocess_2017_1'),
    url(r'^processo/2018', sprocess_2018, name='sprocess_2018'),
]
