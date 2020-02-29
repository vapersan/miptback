from django.core import serializers
from django.http import JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST, require_GET

