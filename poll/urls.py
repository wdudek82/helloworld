from django.conf.urls import url
from . import views

app_name = 'poll'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<id>[\d]+)/$', views.Detail.as_view(), name='detail'),
    url(r'^(?P<id>[\d]+)/result/$', views.Results.as_view(), name='result'),
    url(r'^(?P<id>[\d]+)/vote/$', views.vote, name='vote'),
    # url(r'^(?P<id>[\d]+)/vote/$', views.Vote.as_view(), name='vote'),
]