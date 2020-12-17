from django.contrib import admin
from django.urls import path
from .views import home, contacts, about, login_page, register_page

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home),
    path('contatos', contacts),
    path('sobre', about),

    path('login/', login_page),
    path('registrar/', register_page),

    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)