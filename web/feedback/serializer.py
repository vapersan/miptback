from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, filters
from rest_framework.routers import DefaultRouter

from .models import Feedback
from rest_framework import viewsets


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        # fields = ['text', 'status']
        # read_only_fields = ('id', 'date', 'rate')


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['text']
    filterset_fields = ['status']
    ordering_fields = ['id', 'date', 'rate', 'status']


router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet)
