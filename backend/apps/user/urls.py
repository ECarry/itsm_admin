from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.CreateUserView.as_view()),
    path('verify/email/<email>', views.VerifyEmailCount.as_view()),
    path('verify/username/<username>', views.VerifyUsernameCount.as_view()),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('detail/', views.UserDetailView.as_view())
]
