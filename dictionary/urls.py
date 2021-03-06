from django.conf.urls import url

from . import views

app_name = 'dictionary'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stage/$', views.stage_area, name='stage_area'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^letter/$', views.letter, name='letter'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login_page/$', views.login_page, name='login_page'),
    url(r'^word/(?P<word>.+)/', views.detail_word, name='detail_word'),
    url(r'^accept/(?P<id>\d+)/$', views.accept, name='accept'),
    url(r'^submit/(?P<id_word>[0-9]+)/$', views.submit_word, name='submit_word'),
    url(r'^letter/(?P<lang>[A-Za-z-]+)/$', views.letter, name='letter'),
    url(r'^refuse/(?P<id>\d+)/(?P<redirect>[A-Za-z-]+)/$', views.refuse, name='refuse'),
]
