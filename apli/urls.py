from django.conf.urls import url
from . import views


urlpatterns = [
	
	#DASHBOARD

	url(r'^dashboard$', views.dashboard, name='dashboard'),

	# PERSON: index, 

	url(r'^person$', views.person_index, name='person_index'),
	    # /person/new/
	url(r'^person/(?P<pk>[0-9]+)/$', views.person_detail, name='person_detail'),
	    # /person/new/
    url(r'^person/new/$', views.PersonCreate.as_view(), name='person_new'),
    # /person/<id>/update/
    url(r'^person/(?P<pk>[0-9]+)/create/$', views.PersonCreate.as_view(), name='person_create'),
    # /person/<id>/update/
    url(r'^person/(?P<pk>[0-9]+)/update/$', views.PersonUpdate.as_view(), name='person_update'),
    # /person/<id>/delete/
    url(r'^person/(?P<pk>[0-9]+)/delete/$', views.PersonDelete.as_view(), name='person_delete'),

    # PROJECT
    url(r'^project/$', views.project_index, name='project_index'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.project_detail, name='project_detail'),
]