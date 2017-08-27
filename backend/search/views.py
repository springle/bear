import logging
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import View

from search.models import BerkeleyClass
from search.serializers import BerkeleyClassSerializer, UserSerializer

from rest_framework import viewsets, permissions, filters

class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if your
    staticfiles are in frontend/build/).
    """
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead
		for local development. Or, run `cd frontend && npm run
                build` to test production settings.
                """,
                status=501,
            )

class BerkeleyClassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Courses to be viewed or edited.
    """
    queryset = BerkeleyClass.objects.all().order_by('id')
    serializer_class = BerkeleyClassSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, filters.DjangoFilterBackend)
    search_fields = ('display_name', 'title',)
    ordering_fields = ('id', 'display_name', 'subject',)
    filter_fields = ('enrollment_status_code', 'term', 'waitlisted_count',
                    'component_code', 'subject_code')

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
