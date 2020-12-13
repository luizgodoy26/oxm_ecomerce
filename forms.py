from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form_full_name',
                'placeholder': 'Nome completo'
            }
        )
    )

    email_contact = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'form_email_contact',
                'placeholder': 'E-mail'
            }
        )
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'form_message',
                'placeholder': 'Sua mensagem aqui...'
            }
        )
    )

    # Valida se o e-mail é gmail
    def clean_email_contact(self):
        email_contact = self.cleaned_data.get("email_contact")
        if not "@gmail.com" in email_contact:
            raise forms.ValidationError("E-mail precisa ser gmail!")
        return email_contact


    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        return full_name


    def clean_message(self):
        message = self.cleaned_data.get("message")
        return message
