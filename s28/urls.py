"""s28 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

# from logindemo import views

from bookmanager import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'index/', views.index),
    # url(r'login/', views.login),
    # url(r'db_query/', views.db_query),
    url(r'^publisher_lists/', views.publisher_lists),
    url(r'^publisher_add/', views.publisher_add),
    url(r'^publisher_del/', views.publisher_del),
    url(r'^publisher_change/', views.publisher_change),
    url(r'^bookinfo_lists/', views.bookinfo_lists),
    url(r'^bookinfo_add/', views.bookinfo_add),
    url(r'^bookinfo_del/', views.bookinfo_del),
    url(r'^bookinfo_change/', views.bookinfo_change),
    url(r'^author_lists/', views.author_lists),
    url(r'^author_add/', views.author_add),
    url(r'^author_del/', views.author_del),
    url(r'^author_change/', views.author_change),
    url(r'^template_test/', views.template_test),
]
