from django.urls import path, include
from django.contrib import admin
from feedback.views import *
from .serializer import router

urlpatterns = [
    path('alice/', alice_skill),
    path('api/', include(router.urls)),
    path('api_json_personalInf/', json_resp_api_1),
    path('api_json_study/', json_resp_api_2),
]
