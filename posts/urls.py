from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name="index.html"),
    path('order/', views.order, name="order.html"),
    path('/404', views.page_not_found, name='404.html'),
    path('/500', views.server_error, name='500.html')
]