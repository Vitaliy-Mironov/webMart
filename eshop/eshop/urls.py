from django.conf.urls.static import static
from eshop import settings
from django.contrib import admin
from django.urls import path, include
from shop.views import pageNotFound


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('captcha/', include('captcha.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('shop.urls', namespace='shop')),
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
