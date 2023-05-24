from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_pk>/comment/', views.comment_list),
    path('<int:movie_pk>/comment/', views.comment_post),
    path('<int:movie_pk>/comment/<int:comment_id>/', views.comment_delete),
    path('top_rated/', views.top_rated_list),
    path('popularity/', views.popularity_list),
    path('search/<str:keyword>/', views.search),
    path('likes/<int:movie_id>/', views.likes),
    path('moviecloud/', views.movieCloud),
]
