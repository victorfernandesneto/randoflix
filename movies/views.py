import random
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Movie.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        name = serializer.validated_data['name']
        query = Movie.objects.filter(user=self.request.user).filter(name=name)
        if query:
            raise serializers.ValidationError(
                {'message': 'Movie already registered for this user.'})
        serializer.save(user=self.request.user)


class MovieRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.user != self.request.user:
            raise PermissionDenied("Permission denied.")

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        instance = self.get_object()

        if instance.user != self.request.user:
            raise PermissionDenied("Permission denied.")

        serializer.save()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.user != self.request.user:
            raise PermissionDenied("Permission denied.")

        instance.watched = not instance.watched
        instance.save()

        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class MovieRandomizerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = Movie.objects.filter(
            user=request.user).filter(watched=False)
        if queryset.exists():
            random_movie = random.choice(queryset)
            serializer = MovieSerializer(random_movie)
            return Response(serializer.data)
        else:
            return Response({"message": "No movies available"}, status=404)
