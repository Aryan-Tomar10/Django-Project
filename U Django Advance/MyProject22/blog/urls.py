from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("",PostListView.as_view(), name = "Post_list"),
    path("post/<int:pk>/",PostDetailView.as_view(), name = "Post_detail"),
    path("post/new/",PostCreateView.as_view(), name = "Post_new"),
    path("post/<int:pk>/edit/",PostUpdateView.as_view(), name = "Post_edit"),
    path("post/<int:pk>/delete/",PostDeleteView.as_view(), name = "Post_delete"),
]
