from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = []

router = DefaultRouter()
router.register('area', views.AreaViewSet, basename='area')
urlpatterns += router.urls

