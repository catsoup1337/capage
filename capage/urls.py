from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500
from django.conf import settings

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("", include("posts.urls")),
    path("cart/", include("cart.urls", namespace="cart")),
    path("auth/", include("django.contrib.auth.urls")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler404 = "posts.views.page_not_found"
handler500 = "posts.views.server_error"
