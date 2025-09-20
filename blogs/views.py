from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.


class postlistview(ListView):
    model = Post
    template_name = "post_list.html"


class postdetailview(DetailView):
    model = Post
    template_name = "post_detail.html"
