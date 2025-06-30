from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaFieldViewset


router = DefaultRouter()
router.register(r'files', MediaFieldViewset, basename='media')


urlpatterns = [
    path('', include(router.urls))
]