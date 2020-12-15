from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# Form de login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Form de registro
class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form_register_username',
                'placeholder': 'Nome completo'
            }
        )
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'form_register_email',
                'placeholder': 'E-mail'
            }
        )
    )
    password = forms.CharField(label='Crie sua senha', widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'form_register_p1',
                'placeholder': 'Senha'
            }
        )
    )
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'form_register_p2',
                'placeholder': 'Confirmação de senha'
            }
        )
    )

    def clean(self):
        username = username = self.cleaned_data.get('username')
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            raise forms.ValidationError('Usuário já existe')
        return username

    def clean(self):
        data = self.changed_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Senhas não são correspondentes!")
        return data


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