from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model

# Homepage
def home(request):
    context = {
        "text": "Seja bem vindo!",
    }
    if request.user.is_authenticated:
        context["logged_content"]= "Você está logado!"
    return render(request, 'external/home.html', context)


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
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Erro")
    return render(request, "auth/login.html", context)


# Tela de registro
User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)
