from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import FollowSerializer, ProfileSerializer
from .models import User
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required


from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['GET'])

def profile(request, username):
    person = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(person)
    return Response(serializer.data)

# @api_view(['POST'])
# @login_required
@api_view(['GET'])
# @permission_classes([IsAuthenticated]) # 이게 로그인 한 사용자만 이용할 수 있도록 제한해줌.
def follow(request, user_pk):
    # 현재 로그인한 사용자가 username 사용자를 팔로우/언팔로우
    person = get_user_model().objects.get(pk=user_pk)
    print('펄슨')
    print('--------------------------')
    if request.user != person: # 내가 내 자신을 팔로우 못하게
        # 언팔로우 되어 있으면 팔로우
        # 팔로우 되어 있으면 언팔로우
        
        if request.user in person.followers.all():
            print('팔로우 하고 있음')
            person.followers.remove(request.user)
            
        else:
            print('팔로우 안하고 있음')
            print(request)
            print('--------------------------')
            print(request.user)
            print('--------------------------')
            person.followers.add(request.user)
        print('serializer 먹히는지 보자')
        serializer = FollowSerializer(person)
        print('serializer 과연')
        print(serializer.data)
    return Response(serializer.data)
