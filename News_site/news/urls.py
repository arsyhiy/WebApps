from django.urls import path
from .views import NewsList, NewsDetail, AuthorList, AuthorDetail


urlpatterns =[
  path('NewsList', NewsList.as_view()),
  path('NewsDetail/<int:pk>', NewsDetail.as_view()),
  path('AuthorList', AuthorList.as_view()),
  path('AuthorDetail<int:pk>', AuthorDetail.as_view()),
]