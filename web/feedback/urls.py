from django.urls import path, include

from feedback.views import *
from .serializer import router

urlpatterns = [
    path('api/', include(router.urls)),
]
