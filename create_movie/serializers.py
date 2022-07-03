from django.contrib.auth.models import User, Group
from rest_framework import serializers

from create_movie.models import ImageStock


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageStock
        fields = ('name', 'image')