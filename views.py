from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm
from django.contrib.auth import authenticate, login

# Homepage
def home(request):
    return render(request, 'external/home.html')


# Sobre o site
def about(request):
    return render(request, 'external/about.html')


# Contatos/Entre em contato
def contacts(request):
    contact_from = ContactForm(request.POST or None)
    context= {
        "form": contact_from
    }

    if contact_from.is_valid():
        print(contact_from.cleaned_data)

    if request.method == "POST":
        print(request.POST)
    return render(request, 'external/contacts.html', context)


# Tela de login
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/login")
        else:
            print("Erro")
    return render(request, "auth/login.html", context)


# Tela de registro
def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})
