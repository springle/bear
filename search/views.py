from django.shortcuts import render
from search.models import Course
from search.serializers import CourseSerializer
from rest_framework import viewsets

def index(request):
    context = {}
    return render(request, 'search/index.html', context)

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Courses to be viewed or edited.
    """
    queryset = Course.objects.all().order_by('title')
    serializer_class = CourseSerializer
