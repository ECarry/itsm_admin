from django.urls import path
from . import views

urlpatterns = [
    path('verify/<email>', views.VerifyEmail.as_view())
]
