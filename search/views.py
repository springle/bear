from django.shortcuts import render
from django.contrib.auth.models import User
from search.models import Course
from search.serializers import CourseSerializer, UserSerializer
from rest_framework import viewsets, permissions, filters

def index(request):
    context = {}
    return render(request, 'search/index.html', context)

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ('title',)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
