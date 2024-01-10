from django.urls import path
from .views import (
    PostList, PostDetail,
    CommentList, CommentDetail,
)

urlpatterns = [
    path('post/', PostList.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetail.as_view(), name='post-view'),

    path('comment/', CommentList.as_view(), name='comment-list'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comment-view'),
]