from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('api/', include('blog_api.urls', namespace='blog_api')),
    path('api/users/', include(('users.urls', 'users'), namespace='users_api')),

    path('api_auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path("schema", get_schema_view(
        title='Blog',
        description="Simple Blog API",
        version='1.0'), name="openapi-schema"),
    path('docs/', include_docs_urls(title="BlogAPI"))
]
