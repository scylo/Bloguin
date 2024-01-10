from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post_list", views.post_list, name="post_list"),
    path("post_detail/<int:pk>", views.post_detail, name="post_detail"),
    path("post/add", views.add_post, name="add_post"),
]