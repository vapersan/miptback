from django.urls import path, include

from feedback.views import *
from .serializer import router

urlpatterns = [
    path('alice/', alice_skill),
    path('api/', include(router.urls)),
]
