from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'external/home.html')

def about(request):
    return render(request, 'external/about.html')

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