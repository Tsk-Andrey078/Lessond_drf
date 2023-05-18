from django.urls import path
from lessond_drf import views

urlpatterns = [
    path('get_news/', views.ListInfo.as_view()),
]