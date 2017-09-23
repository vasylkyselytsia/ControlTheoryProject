from django.conf.urls import url, include
from core.landing import urls as landing
from core.service import urls as service
from core.auth import urls as auth

urlpatterns = [
    url(r'^', include(landing, namespace="landing")),
    url(r'^service/', include(service, namespace="service")),
    url(r'^auth/', include(auth)),
]
