from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from rest_framework.response import Response
from .serializers import FollowSerializer, ProfileSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@require_safe
def profile(request, username):
    person = get_user_model().object.get(username=username)
    serializer = ProfileSerializer(person)
    return Response(serializer.data)


@require_POST
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    # 현재 로그인한 사용자가 user_pk 사용자를 팔로우/언팔로우
    person = get_user_model().objects.get(pk=user_pk)
    if request.user != person:
        # 언팔로우 되어 있으면 팔로우
        # 팔로우 되어 있으면 언팔로우
        if request.user in person.followers.all():
            person.followers.remove(request.user)
            
        else:
            person.followers.add(request.user)

        serializer = FollowSerializer(person)
    return Response(serializer.data)
