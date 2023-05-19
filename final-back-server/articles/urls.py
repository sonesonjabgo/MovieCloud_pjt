from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comment/', views.comment_list),
    path('<int:article_pk>/comment/post/', views.comment_post),
    path('<int:article_pk>/comment/<int:comment_id>/', views.comment_delete),
]
