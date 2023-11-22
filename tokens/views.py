from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')

        query1 = User.objects.filter(username=username).first()
        query2 = User.objects.filter(email=email).first()

        if query1 or query2:
            return JsonResponse(
                {'message': 'Username or email already registered'}
            )

        password = request.data.get('password')

        User.objects.create_user(
            username=username, email=email, password=password)
        user = User.objects.filter(username=username).first()
        return JsonResponse(
            {'id': user.id,
             'username': user.username,
             'email': user.email, }
        )
