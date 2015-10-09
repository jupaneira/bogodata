from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.images, name='images'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.inseguro, name='inseguro'),
]
