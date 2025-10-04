from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                    )


# Create your views here.


class postlistview(ListView):
    model = Post
    template_name = "post_list.html"


class postdetailview(DetailView):
    model = Post
    template_name = "post_detail.html"

class postcreateview(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title', 'content', 'author']

class postupdateview(UpdateView):
    model = Post
    template_name = "post-update.html"
    fields = ['title', 'content']

class postdeleteview(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post-list") # Redirect to home page after deletion