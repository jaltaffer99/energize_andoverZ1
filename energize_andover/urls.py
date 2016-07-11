from django.conf.urls import url
from . import views

app_name = 'energize_andover'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Graph', views.grapher, name='graph'),
]
