from django.shortcuts import render
from django.contrib.auth.models import User
from search.models import Course
from rest_framework import viewsets
from search.serializers import CourseSerializer, UserSerializer

def index(request):
    context = {}
    return render(request, 'search/index.html', context)

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Courses to be viewed or edited.
    """
    queryset = Course.objects.all().order_by('title')
    serializer_class = CourseSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
