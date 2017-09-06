from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
