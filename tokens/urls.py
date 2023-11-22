from django.urls import path
from tokens.views import LoginView, RegisterView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login_view'),
    path('register/', RegisterView.as_view(), name='register_view'),
]
