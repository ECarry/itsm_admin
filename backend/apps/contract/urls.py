from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContractList.as_view()),
    path('create/', views.ContractCreate.as_view()),
    path('<int:pk>', views.ContractDetail.as_view()),
    path('<label>/<value>/', views.ContractSearch.as_view())
]