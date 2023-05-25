from django.shortcuts import render
from django.conf import settings
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# 전체 articles 조회 및 생성
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        # user_id를 통해서 username 얻어내야 함
        # 이건 accounts 완성 후 수정
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# article 세부 정보 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# 단일 article의 comment 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comment_list(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.article_comments.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 코멘트 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_post(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# 코멘트 삭제
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, article_pk, comment_id):
    article = Article.objects.get(pk=article_pk)
    comment = article.article_comments.all().get(id=comment_id)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# 좋아요 기능
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return Response({'result':'success'})
    return Response({'result':'login_required'})