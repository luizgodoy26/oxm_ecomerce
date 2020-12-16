from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


# Form de login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



# Form de registro
class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Senhas tem de ser iguais')
        return data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Usuário já está em uso')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('E-mail já está em uso')
        return email


# Form de contato
class ContactForm(forms.Form):
    full_name = forms.CharField(
        label='Seu nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form_full_name',
                'placeholder': 'Nome completo'
            }
        )
    )

    email_contact = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'form_email_contact',
                'placeholder': 'E-mail'
            }
        )
    )

    message = forms.CharField(
        label='Sua mensagem',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'form_message',
                'placeholder': 'Sua mensagem aqui...'
            }
        )
    )

    def clean_email_contact(self):
        email_contact = self.cleaned_data.get("email_contact")
        # Valida se o e-mail é gmail
        if not "@gmail.com" in email_contact:
            raise forms.ValidationError("E-mail precisa ser gmail!")
        return email_contact

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        return full_name

    def clean_message(self):
        message = self.cleaned_data.get("message")
        return message