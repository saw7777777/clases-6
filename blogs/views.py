from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

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