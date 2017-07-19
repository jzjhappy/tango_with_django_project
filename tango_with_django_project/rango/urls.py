'''
Created on Jul 12, 2017

@author: jwang02
'''
from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'), 
    url(r'^category/(?P<category_hashed_name_as_url>\w+)/$', views.category, name='category'),
    url(r'^category/(?P<category_hashed_name_as_url>\w+)/add_page/$', views.add_page, name='add_page'),
]
