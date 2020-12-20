from django.contrib import admin
from django.urls import path, include
from .views import home, contacts, about, login_page, register_page
from products import urls as products_urls

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home),
    path('contatos', contacts),
    path('sobre', about),

    path('admin/', admin.site.urls),

    # Auth
    path('login/', login_page),
    path('registrar/', register_page),

    # Produtos
    path('produtos/', include(products_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG == True:
#     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
#     static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)