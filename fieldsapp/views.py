from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')