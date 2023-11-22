from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import JsonResponse


class MovieListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # Your code here
        return JsonResponse({"response":"YOU ARE ALLOWED HERE"})