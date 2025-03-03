from django.urls import path
from . import views
from django.urls import re_path as url

urlpatterns = [ 
    path('', views.PostView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('review/<int:pk>', views.AddComments.as_view(), name='add_commetns'),

    path('<int:pk>/add_likes', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes', views.delLike.as_view(), name='dell_likes'),
                ]


