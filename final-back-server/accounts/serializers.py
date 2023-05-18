from rest_framework import serializers
from .models import User

class FollowSerializer(serializers.ModelSerializer):
    following_count = serializers.IntegerField(source='followings', read_only=True)
    follower_count = serializers.IntegerField(source='followers.count', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name',)

