from django.urls import path
from . import views

urlpatterns = [ 
    
    # URL to open page
    path("", views.home, name='home')
]
