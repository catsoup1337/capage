from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name="index.html"),
    path('order/', views.order, name="order.html"),
    path('item/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'), 
]