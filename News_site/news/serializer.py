from rest_framework import serializers
from news.models import News, Author

class NewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = News
    fields = ('__all__')
    depth = 1

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ('__all__')
    depth = 1