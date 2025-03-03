from rest_framework import generics
from .models import Movie
from .serializers import MovieSeriaLizer
from rest_framework.response import Response


class MovieListCreateView(generics.ListCreateAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSeriaLizer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSeriaLizer


class AllMoviesListView(generics.ListAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSeriaLizer


class MovieUpdateView(generics.RetrieveUpdateAPIView):
  queryset=  Movie.objects.all()
  serializer_class = MovieSeriaLizer
  partial = True


class MovieDeleteView(generics.DestroyAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSeriaLizer

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.delete()
    return Response(print("delete movie"))