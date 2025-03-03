from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path, include


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(),
        name='snippet-detail'),
    path('users/<int:pk>/', views.UserDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighLight.as_view(),
        name='snippet-highlight'),
    path('users/', views.UserList.as_view(),
        name='user-list'),
        path('users/<int:pk>/', views.UserDetail.as_view(),
            name='user-detail')
])
