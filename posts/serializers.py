from rest_framework import serializers

from accounts.models import CustomUser
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', queryset=CustomUser.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'body', 'author', 'created_at')
