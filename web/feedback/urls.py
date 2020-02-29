from django.urls import path, include
from django.contrib import admin
from feedback.views import *
from .serializer import router

urlpatterns = [
    path('alice/', alice_skill),
    path('api/', include(router.urls)),
]
