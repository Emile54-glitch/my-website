from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    # URL pattern for the list of blog posts.
    path('', BlogListView.as_view(), name='blog-list'),

    # URL pattern for displaying an individual blog post, where <int:pk> captures the post's primary key.
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]