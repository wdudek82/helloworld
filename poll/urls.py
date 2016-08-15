from django.conf.urls import url
from . import views

app_name = 'poll'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.Detail.as_view(), name='detail'),
]