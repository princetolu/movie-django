from django.shortcuts import render
from .models import Post
from rest_framework import viewsets
from .serializer import PostSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
