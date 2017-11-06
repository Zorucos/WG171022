from django.conf.urls import url
from . import views


urlpatterns = [

   #ASSIGNMENT: index, detail, create, update, delete.

    url(r'^assignment/$', views.assignment_index, name='assignment_index'),

    url(r'^assignment/(?P<pk>[0-9]+)/$', views.assignment_detail, name='assignment_detail'),
    url(r'^assignment/new/$', views.AssignmentCreate.as_view(), name='assignment_new'),
    url(r'^assignment/(?P<pk>[0-9]+)/update/$', views.AssignmentUpdate.as_view(), name='assignment_update'),
    url(r'^assignment/(?P<pk>[0-9]+)/delete/$', views.AssignmentDelete.as_view(), name='assignment_delete'),
    #url(r'^assignment/(?P<pk>[0-9]+)/send/$', views.Assignment_send, name='assignment_send'),
	
	#DASHBOARD: index
	url(r'^dashboard$', views.dashboard, name='dashboard'),

	# PERSON: index, detail, create, update, delete.

	url(r'^person$', views.person_index, name='person_index'),

	url(r'^person/(?P<pk>[0-9]+)/$', views.person_detail, name='person_detail'),
    url(r'^person/new/$', views.PersonCreate.as_view(), name='person_new'),
    url(r'^person/(?P<pk>[0-9]+)/update/$', views.PersonUpdate.as_view(), name='person_update'),
    url(r'^person/(?P<pk>[0-9]+)/delete/$', views.PersonDelete.as_view(), name='person_delete'),

    # PROJECT: index, detail, create, update, delete.

    url(r'^project/$', views.project_index, name='project_index'),

    url(r'^project/(?P<pk>[0-9]+)/$', views.project_detail, name='project_detail'),
    url(r'^project/new/$', views.ProjectCreate.as_view(), name='project_new'),
    url(r'^project/(?P<pk>[0-9]+)/update/$', views.ProjectUpdate.as_view(), name='project_update'),
    url(r'^project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='project_delete'),


]