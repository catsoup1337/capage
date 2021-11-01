from django.urls import path

from . import views
from cart import views as cart_views

urlpatterns = [

    path('', views.home_view, name="index.html"),
    path('order/', views.order, name="order.html"),
    path('item/<int:pk>/', views.post_detail, name='post_detail'),
    path('checkout', cart_views.get_checkout, name="checkout"),
    path('make-order/', cart_views.make_order, name='make_order')
]
