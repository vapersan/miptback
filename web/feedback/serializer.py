from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, filters
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter

from .models import Feedback, Teacher


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

    def update(self, request, *args, **kwargs):
        # Обновление по частям
        # https://www.django-rest-framework.org/api-guide/serializers/#partial-updates
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']

    # filterset_fields = ['status']
    # ordering_fields = ['id', 'date', 'rate', 'status']

    def update(self, request, *args, **kwargs):
        # Обновление по частям
        # https://www.django-rest-framework.org/api-guide/serializers/#partial-updates
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet)
router.register(r'teacher', TeacherViewSet)
