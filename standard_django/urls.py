"""standard_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include

"""
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic.base import TemplateView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

from product.views import ProductListAPIView,PostCreateAPIView, ProductDetailAPIView, ProductUpdateAPIView, \
    ProductDeleteAPIView
from users import views as user_views

from users.views import AngularTemplateView

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^templatess/(?P<item>[A-Za-z0-9\_\-\.\/]+)\.html$', AngularTemplateView.as_view()),
    url(r'^api/users/', include("users.urls", namespace='users-api')),
    url(r'^admin/logout$', user_views.logout_view, name='logout'),

    url(r'^api/product/$', ProductListAPIView.as_view()),
    url(r'^api/product/(?P<id>[0-9]+)/$', ProductDetailAPIView.as_view(), name='detail'),

    url(r'^api/product/(?P<id>[0-9]+)/edit/$', ProductUpdateAPIView.as_view(), name='detail'),

    url(r'^api/product/add/', PostCreateAPIView.as_view()),

    url(r'^api/product/(?P<id>[0-9]+)/delete/$', ProductDeleteAPIView.as_view(), name='delete'),

]

urlpatterns += [
    url(r'', TemplateView.as_view(template_name='index.html'))
]
