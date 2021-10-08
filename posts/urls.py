from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name="index.html"),
    path('order/', views.order, name="order.html"),
    path('item/<int:pk>/', views.post_detail, name='post_detail'), 
]