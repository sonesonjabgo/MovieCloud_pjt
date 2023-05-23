from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import FollowSerializer
from .models import User
from rest_framework.decorators import api_view


from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['GET'])
def profile(request, username):
    # username으로 들어가서 이 username을 가진 사용자의 프로필을 보여줌
    person = get_object_or_404(User, username=username)
    serializer = FollowSerializer(person)
    return Response(serializer.data)

@api_view(['GET'])
def user_info(request, user_pk): # 
    # username으로 들어가서 이 username을 가진 사용자의 프로필을 보여줌
    person = get_object_or_404(User, pk=user_pk)
    serializer = FollowSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 이게 로그인 한 사용자만 이용할 수 있도록 제한해줌.
def follow(request, user_pk):
    # 현재 로그인한 사용자가 username 사용자를 팔로우/언팔로우
    person = get_user_model().objects.get(pk=user_pk)

    if request.user != person: # 내가 내 자신을 팔로우 못하게
        # 언팔로우 되어 있으면 팔로우
        # 팔로우 되어 있으면 언팔로우
        
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)

        serializer = FollowSerializer(person)
    return Response(serializer.data)


