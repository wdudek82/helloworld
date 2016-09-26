from django.conf.urls import url

from . import views

app_name = 'app1'

urlpatterns = [
    # Static pages
    url(r'^boot/', views.Boot.as_view(), name='boot'),
    url(r'^portfolio/', views.Portfolio.as_view(), name='portfolio'),
    url(r'^btutorial/', views.Btutorial.as_view(), name='btutorial'),

    # url(r'^create/', views.ExampleCreate.as_view(), name='ocreate'),
    # url(r'^(?P<slug>[\w-]+)/', views.ExampleDetail.as_view(), name='oexample'),

    url(r'^mobitest/', views.MobiriseTest.as_view(), name='mobitest'),

    # url(r'^create/$', views.example_create, name='create'),
    # url(r'^(?P<slug>[\w-]+)/$', views.example, name='example'),
]
