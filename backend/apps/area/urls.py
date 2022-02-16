from django.urls import path
from . import views

urlpatterns = [
    path('province/', views.ProvinceListView.as_view()),
    path('province/<pk>', views.ProvinceDetailListView.as_view())
]