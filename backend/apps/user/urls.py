from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view()),
    path('verify/email/<email>', views.VerifyEmailCount.as_view())
]