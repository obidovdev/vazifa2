from django.urls import path, include

from . import views
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('created/', post_created, name='created_post')


]