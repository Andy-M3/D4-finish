from django.urls import path
from .views import (
    NewsDetail, NewsCreate, NewsList, Search, NewsUpdate, NewsDelete
)

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('search/', Search.as_view(), name='search'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]