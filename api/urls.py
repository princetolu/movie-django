from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet

router=routers.DefaultRouter()
router.register('post', PostViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
]