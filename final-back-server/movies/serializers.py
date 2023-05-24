from rest_framework import serializers
from .models import Movie, Movie_Comment


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['comments_users']


