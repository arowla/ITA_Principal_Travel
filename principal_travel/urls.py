"""principal_travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from travel.views import TripViewSet
from travel.views import EventLocationPrincipalTravelList
from travel.views import EventLocationPrincipalTravelDetail
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'trips', TripViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^itineraries/$', EventLocationPrincipalTravelList.as_view()),
    url(r'^itineraries/(?P<pk>[0-9]+)/$', EventLocationPrincipalTravelDetail.as_view())
]
