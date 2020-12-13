from django.contrib import admin
from django.urls import path
from .views import home, contacts, about

urlpatterns = [
    path('', home),
    path('contatos', contacts),
    path('sobre', about),

    path('admin/', admin.site.urls),
]
