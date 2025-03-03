from .models import Author, News
from rest_framework import generics
from news.serializer import NewsSerializer, AuthorSerializer
from rest_framework import permissions

class NewsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = NewsSerializer
    queryset = News.objects.all()
class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Author.objects.all()

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()