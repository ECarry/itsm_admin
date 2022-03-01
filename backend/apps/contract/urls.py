from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContractListView.as_view()),
    path('create/', views.CreateContractView.as_view())
]