from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', include('vocab.urls')),
    path('', include("user_account.urls")),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
