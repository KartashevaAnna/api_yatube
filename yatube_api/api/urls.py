from django.urls import include, path
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('api/v1/groups', GroupViewSet)
router.register('api/v1/posts', PostViewSet)
router.register(r'api/v1/posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),

]