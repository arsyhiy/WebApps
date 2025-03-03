from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    ############################################################################
    path('', views.index, name="todo"),
    ###########################################################################
    # pass item_idas primary key to remove that  the todo with given id 
    path('del/<str:item_id>', views.remove, name="del"),
    ########################################################################### 
    path('admin/', admin.site.urls),

]
