from django.conf.urls import url
from . import views

app_name = 'app1'

urlpatterns = [
    url(r'^boot/', views.Boot.as_view(), name='boot'),
    url(r'^create/', views.ExampleCreate.as_view(), name='ocreate'),
    url(r'^(?P<slug>[\w-]+)/', views.ExampleDetail.as_view(), name='oexample'),


    # url(r'^create/$', views.example_create, name='create'),
    # url(r'^(?P<slug>[\w-]+)/$', views.example, name='example'),
]
