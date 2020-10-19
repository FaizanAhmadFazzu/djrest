from .views import GenericAPIView
from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter
 
 
router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('article/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls))
]