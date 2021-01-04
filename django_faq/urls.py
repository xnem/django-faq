from django.conf.urls import url
from . import views


urlpatterns = [
    url('insert/', views.insert),
    url('update/', views.update),
    url('search/', views.search),
    url('delete/', views.delete),
    url('lock/', views.lock),
    url('unlock', views.unlock),
    url('check/', views.check)
]