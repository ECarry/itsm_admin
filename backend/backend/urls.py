from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/', include('verify_email.urls')),
    path('user/', include('user.urls')),
    path('area/', include('area.urls'))
]
