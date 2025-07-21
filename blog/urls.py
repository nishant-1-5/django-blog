from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('', views.home, name='blog-home'), function view
    path('about/', views.about, name='blog-about'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('', PostListView.as_view(), name='blog-home'), # class based view
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts') 
]

# looks for template <app>/<model>_<viewtype>.html by default