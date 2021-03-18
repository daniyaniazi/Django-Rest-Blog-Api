from django.urls import path
from .views import PostList, UserPostList, PostDetailList
from rest_framework.routers import DefaultRouter


app_name = "blog"

# router = DefaultRouter()
# router.register("", PostList, basename="post")

# urlpatterns = router.urls
urlpatterns = [
    path('my_posts/', UserPostList.as_view(), name='user_posts'),
    path('my_posts/<str:pk>/', PostDetailList.as_view(), name='user_post_detail'),
    #     # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    #     # path('', PostList.as_view(), name='listcreate'),

]
