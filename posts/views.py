from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from cart.forms import CartAddProductForm
from .models import Post
 
 
class BlogListView(ListView):
    model = Post
    template_name = 'index.html'
 

def order(request):
    return render(request, 'order.html')


# class BlogDetailView(DetailView): 
#     model = Post
#     cart_product_form = CartAddProductForm()
#     template_name = 'post_detail.html'
#     return render(request, 'post_detail.html', {'post': post, 'cart_product_form': cart_product_form, })

def post_detail(request, pk,):
    post = get_object_or_404(Post,
                                pk=pk,
                                )
    cart_product_form = CartAddProductForm()
    return render(request, 'post_detail.html', {'post': post,
                                                        'cart_product_form': cart_product_form})

def page_not_found(request,exception):
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500)
