from django.conf.urls import patterns, include, url
from django.contrib import admin
from landing import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', views.PersonCreate.as_view(), name='homepage'),
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),

    url(r'^form/', views.person_create, name='person_create'),


)
