"""definiuje wzorce adresow URL dla learning_logs"""

from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    #strona glowna
    url(r'^$', views.index, name = 'index',),

    #wyświetlanie wszystkich tematów
    url(r'^topics/$', views.topics, name = 'topics'),
]
