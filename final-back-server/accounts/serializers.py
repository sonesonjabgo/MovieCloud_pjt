from rest_framework import serializers
from .models import User

class FollowSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField()
    follower_count = serializers.SerializerMethodField()

    def get_following_count(self, obj):
        return obj.followings.count()

    def get_follower_count(self, obj):
        return obj.followers.count()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'following_count', 'follower_count',)


# class ProfileSerializer(serializers.ModelSerializer):
#     following_count = serializers.SerializerMethodField()
#     follower_count = serializers.SerializerMethodField()

#     def get_following_count(self, obj):
#         return obj.followings.count()

#     def get_follower_count(self, obj):
#         return obj.followers.count()
    
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password', 'first_name', 'following_count', 'follower_count',)
