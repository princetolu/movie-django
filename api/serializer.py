from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'cover', 'video_link', 'year', 'mins', 'rating', 'bg_img', 'genere', 'date')