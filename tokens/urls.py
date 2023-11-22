from django.urls import path
from tokens.views import LoginView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login_view')
]