from rest_framework import generics, permissions
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly,  AllowAny, IsAuthenticated, BasePermission
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.


class PostUserWritePermission(BasePermission):
    message = 'Editing Posts is restricted to the author only'

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    #queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    # When kwargs are present

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    # Fired oN ROOT directory
    def get_queryset(self):
        return Post.objects.all()


class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class PostDetailList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs['pk']
        return Post.objects.filter(slug=slug)


# # class PostList(generics.ListCreateAPIView):
# class PostList(viewsets.ViewSet):
#     permission_classes = [AllowAny]
#     queryset = Post.postobjects.all()
#     # serializer_class = PostSerializer

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     # Single item
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):


# class PostDetail(viewsets.ViewSet, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
