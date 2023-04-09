from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('', include('about.urls')),
    path('', include('social_media.urls')),
    path('book-form/', include('bookform.urls')),
    path('auth/', include('authorization.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt",
    content_type='text/plain')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'scottys.views.error_404'
