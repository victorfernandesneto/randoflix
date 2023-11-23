from django.urls import path
from tokens.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('authentication/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/token/verify/',
         TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='register_view'),
]
