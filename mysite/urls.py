"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from conference.views import Main_view, speakers_do, reports_info, reports_new, reports_edit, post_draft_list, \
    reports_publish, reports_remove

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Main_view, name="Main_view"),  # список спикеров и инфы о них
    url(r'^speakers/(?P<pk>\d+)/$', speakers_do, name="speakers_do"),  # спикер и доклады которые он читает
    url(r'^reports/info/(?P<pk>\d+)/$', reports_info, name="reports_info"),  # информация о докладе
    url(r'^/new/$', reports_new, name='reports_new'),
    url(r'^reports/(?P<pk>\d+)/edit/$', reports_edit, name='reports_edit'),
    url(r'^drafts/$', post_draft_list, name='post_draft_list'),
    url(r'^reports/(?P<pk>\d+)/publish/$', reports_publish, name='reports_publish'),
    url(r'^reports/(?P<pk>\d+)/remove/$', reports_remove, name='reports_remove'),

]
# name='____' — это имя URL, которое будет использовано, чтобы идентифицировать его.
