from django.urls import path
from .views import EventViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='events')
router.register(r'register', UserViewSet, basename='register')

urlpatterns = router.urls
