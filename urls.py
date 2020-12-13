from django.contrib import admin
from django.urls import path
from .views import home, contacts, about, login_page

urlpatterns = [
    path('', home),
    path('contatos', contacts),
    path('sobre', about),

    path('login/', login_page),

    path('admin/', admin.site.urls),
]
