from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
	path('',views.HomePage),
    url(r'^api/dev',views.ApiFirst.as_view(),name="ApiFirst"),
    url(r'^api/org',views.ApiSecond.as_view(),name="ApiSecond"),
]
