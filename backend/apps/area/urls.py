from django.urls import path
from . import views

urlpatterns = [
    path('province/', views.AreaListView.as_view()),
    path('province/<pk>', views.AreaDetailListView.as_view())
]