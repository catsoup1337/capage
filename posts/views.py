from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Post, News

class NewsListView(ListView):
    model = News
    template_name = 'index.html'


class BlogListView(ListView):
    model = Post
    template_name = 'index.html'


def order(request):
    return render(request, 'order.html')


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
