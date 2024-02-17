from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import permissions
# from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthorOrReadOnly,)
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # permission_classes = (permissions.IsAdminUser,)
#     permission_classes = (IsAuthorOrReadOnly,)
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
