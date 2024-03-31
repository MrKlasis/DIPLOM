from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from app_users.apps import AppUsersConfig
from app_users.views.views_api import RegisterUserAPIView, ProfileAPIView, PhoneAPIView, VerifyPhoneAPIView

app_name = AppUsersConfig.name

urlpatterns = [
    # Registration
    path('register/', RegisterUserAPIView.as_view(), name="register"),

    # Verify phone
    path('phone/', PhoneAPIView.as_view(), name="phone"),
    path('code/<int:pk>/', VerifyPhoneAPIView.as_view(), name="code"),

    # Authorization
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    # Profile
    path('profile/<int:pk>/', ProfileAPIView.as_view(), name='profile'),

]
