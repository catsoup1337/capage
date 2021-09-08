from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
 
 
class BlogListView(ListView):
    model = Post
    template_name = 'index.html'
 

def order(request):
    return render(request, 'order.html')


class BlogDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'


def page_not_found(request,exception):
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500)
