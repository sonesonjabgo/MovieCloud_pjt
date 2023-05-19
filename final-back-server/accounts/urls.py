from django.urls import path
from . import views


urlpatterns = [
    path('<str:username>/', views.profile),
    path('<int:user_pk>/follow/', views.follow)

]



    