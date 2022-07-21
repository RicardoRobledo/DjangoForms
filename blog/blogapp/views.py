from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView, DetailView
from django.urls import reverse_lazy # new


# Create your views here.
class BlogListView(ListView):
    
    model = Post
    template_name = 'blogapp/home.html'
    context_object_name = 'all_posts_list'


class BlogDetailView(DetailView):
    
    model = Post
    template_name = 'blogapp/post_detail.html'


class BlogCreateView(CreateView):

    model = Post
    template_name = 'blogapp/post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'blogapp/post_edit.html'
    
    # We are explicitly listing the fields we want to use ['title', 'body'] rather than using '__all__'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):

    model = Post
    template_name = 'blogapp/post_delete.html'
    success_url = reverse_lazy('blogapp:home')


class About(TemplateView):
    
    model = Post
    template_name = 'blogapp/about.html'
