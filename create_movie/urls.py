from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('upload-image/', views.ImageViewSet.as_view(), name='upload'),
    
]