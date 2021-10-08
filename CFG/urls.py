"""CFG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url
from education.views import (
    RegionViewSet,
    HouseHoldViewSet,
    SchoolViewSet
)


router = DefaultRouter()
router.register(r"regions", RegionViewSet)
router.register(r"households", HouseHoldViewSet)
router.register(r"schools", SchoolViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    url(r'^favicon\.ico$',RedirectView.as_view(url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.jpmorganchase.com%2Fnews-stories%2Ffive-things-you-need-to-know-about-code-for-good&psig=AOvVaw1cRD7sD1Y1bSecvp-KuC5C&ust=1633813423751000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPiYuLjbu_MCFQAAAAAdAAAAABAD"))
]
