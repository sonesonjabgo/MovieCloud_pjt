from rest_framework import serializers
from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     followings = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

#     class Meta:
#         model = User
#         fields = ('followings')

class FollowSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField()
    follower_count = serializers.SerializerMethodField()
    # following_list = UserSerializer(many=True)

    def get_following_count(self, obj):
        return obj.followings.count()

    def get_follower_count(self, obj):
        return obj.followers.count()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'following_count', 'follower_count', 'followings', 'like_movies')

# class FollowSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password', 'first_name', 'following_count', 'follower_count',)
