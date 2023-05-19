from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer, MovieListSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
from django.shortcuts import get_object_or_404

# 전체 리스트 조회
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 영화 세부정보
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 단일 영화의 코멘트 리스트 조회
# post는 로그인 확인이 필요함. (accounts 완료되면 수정)
@api_view(['GET'])
def comment_list(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.movie_comments.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 코멘트 생성
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_post(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 코멘트 삭제
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def comment_delete(request, movie_pk, comment_id):
    movie = Movie.objects.get(pk=movie_pk)
    comment = movie.movie_comments.all().get(id=comment_id)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# 전체 영화 중 vote_average 기준 상위 10개 넘겨주는 view
@api_view(['GET'])
def top_rated_list(request):
    movies = Movie.objects.all()
    movies = sorted(movies, key=lambda movies: movies.vote_average, reverse=True)[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 전체 영화 중 popularity 기준 상위 10개 넘겨주는 view
@api_view(['GET'])
def popularity_list(request):
    movies = Movie.objects.all()
    movies = sorted(movies, key=lambda movies: movies.popularity, reverse=True)[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 제목 검색 기능
@api_view(['GET'])
def search(request, keyword):
    movies = Movie.objects.all()
    search_list = []
    # 전체 영화에서 title에 keyword가 들어가면 search_list에 추가
    for movie in movies:
        if keyword in movie.title or keyword in movie.overview:
            search_list.append(movie)
    serializer = MovieListSerializer(search_list, many=True)
    return Response(serializer.data)