from rest_framework import serializers
from search.models import BerkeleyClass
from django.contrib.auth.models import User

class BerkeleyClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BerkeleyClass
        fields = ('title', 'description')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
