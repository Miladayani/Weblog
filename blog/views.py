from django .views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-date_time_modified')
#
class PostDetailView(generic.DetailView):
    template_name = 'blog/posts_detail.html'
    model = Post
    context_object_name = 'post'

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/add_post.html'

# /blog/edit/10
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')
