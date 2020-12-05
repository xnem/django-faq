from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url('api/', include('django_faq.urls'))
]
