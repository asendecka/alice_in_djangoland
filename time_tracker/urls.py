from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.work_done_edit, name='work_done_edit'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.work_done_edit, name='work_done_edit'),
    url(r'^list/$', views.work_done_list, name='work_done_list'),
]
