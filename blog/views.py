from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User 
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'This is the content of blog post 1.',
        'date_posted': '2023-10-01'
    },
    {
        'author': 'Jane Smith',
        'title': 'Blog Post 2',
        'content': 'This is the content of blog post 2.',
        'date_posted': '2023-10-02'
    }
] # assume made a db call to get posts


# # static
# def home(request):
#     return render(request, 'blog/home.html')

# #static
# def about(request):
#     return render(request, 'blog/about.html')


# dynamic
def home(request):
    # create a context 
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context) # passes data to the template and can use there

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # template
    context_object_name = 'posts' # what to loop over
    ordering = ['-date_posted'] # how to order - = DESC
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] 
    paginate_by = 5
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name='blog/post-detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # override this method to auto provide the author
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # override this method to auto provide the author
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# dynamic
def about(request):
    context = {
        'title': 'About Us',
        'content': 'This is the about page.'
    }
    return render(request, 'blog/about.html', context)