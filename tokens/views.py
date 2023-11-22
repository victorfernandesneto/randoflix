from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username, password=password)

        refresh = RefreshToken.for_user(user)

        return JsonResponse(
            {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        )