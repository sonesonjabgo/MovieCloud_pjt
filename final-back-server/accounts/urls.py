from django.urls import path, include
from . import views


urlpatterns = [
    path('',include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('<str:username>/', views.profile),
    path('<int:user_pk>/info/', views.user_info),
    path('<int:user_pk>/follow/', views.follow),

]



    