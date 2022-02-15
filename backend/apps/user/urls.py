from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('create/', views.CreateUserView.as_view()),
    path('verify/email/<email>', views.VerifyEmailCount.as_view()),
    path('verify/username/<username>', views.VerifyUsernameCount.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]