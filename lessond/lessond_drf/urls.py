from django.urls import path
from lessond_drf import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('get_news/', views.ListInfo.as_view()),
    path('get_news_list/', views.NewsViewSet.as_view({'get':'list'})),
    path('update_news/', views.NewsViewSet.as_view({'post':'update'})),
    path('delete_news/', views.NewsViewSet.as_view({'post':'delete_news'})),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]