from rest_framework import routers
from django.urls import path, include
from session_app_tracker.api import viewsets as userviewsets

router = routers.DefaultRouter()
router.register(r'users', userviewsets.UserViewSets, basename="Users")

urlpatterns = [
    path('', include(router.urls)),
]