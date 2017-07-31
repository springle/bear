from rest_framework import serializers
from search.models import BerkeleyClass
from django.contrib.auth.models import User

class BerkeleyClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BerkeleyClass
        fields = ('id', 'display_name', 'term', 'term_name', 'title', 'number',
            'offering_number', 'description', 'subject_code', 'subject',
            'enrolled_count', 'waitlisted_count', 'min_enroll', 'max_enroll',
            'max_waitlist', 'component_code', 'component',
            'enrollment_status_code', 'enrollment_status', 'date_created',
            'date_updated')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
