from rest_framework import generics, permissions
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission
# Create your views here.


class PostUserWritePermission(BasePermission):
    message = 'Editing Posts is restricted to the author only'

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


# class PostList(generics.ListCreateAPIView):
class PostList(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):


class PostDetail(viewsets.ModelViewSet,PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
