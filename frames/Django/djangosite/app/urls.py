from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'moments_input', views.moments_input),
	url(r'', views.welcome, name='first-url'),

#	path(r'year/2018', views.moments_2018),
#	url(r'^year/([0-9]{4})/$', views.year_moments),
#	url(r'^year/([0-9]{4})/([0-9]{2})/$', views.year_moments),
#	url(r'^year/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.year_moments),
#	url(r'^year/?P<year>([0-9]{4})/$', views.year_moments),
#	url(r'^year/?P<year>([0-9]{4})/?P<month>([0-9]{2})/$', views.year_moments),
]