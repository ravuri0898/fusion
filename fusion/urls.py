from django.conf.urls import url
from . import views

app_name = 'fusion'

urlpatterns = [
    # fusion/
    url(r'^$', views.index, name='index'),

    # fusion/login/
    url(r'^login$', views.login, name='login'),

    # fusion/login/
    url(r'^temp$', views.temp, name='temp'),

    # fusion/home/<pk>/
    url(r'^home/(?P<emp_id>[0-9]+)$', views.home, name='home'),

    # fusion/profile/<pk>/
    url(r'^profile/(?P<emp_id>[0-9]+)$', views.profile, name='profile'),

    # fusion/dashboard/<pk>/
    url(r'^dashboard/(?P<emp_id>[0-9]+)$', views.dashboard, name='dashboard'),
]
