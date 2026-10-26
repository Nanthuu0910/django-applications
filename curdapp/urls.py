from django.urls import path
from curdapp.views import *
 
urlpatterns=[
    path('',home,name='home'),
    path('read/',read,name='read'),
    path('create/',create,name='create'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',deletestudent,name='delete'),
    

]