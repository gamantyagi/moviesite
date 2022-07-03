import json
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from create_movie.models import ImageStock
from .serializers import ImageSerializer, UserSerializer, GroupSerializer

def index(request):
    return HttpResponse("Here we go again!!")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ImageViewSet(ListAPIView):
    queryset = ImageStock.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['image']
        name = request.data['name']
        image = ImageStock.objects.create(image=file, name=name)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)