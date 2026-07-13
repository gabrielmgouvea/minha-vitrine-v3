from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models import Avaliacao, Feedback


class RegistroForm(UserCreationForm):
    """Formulário de registro de usuários"""
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label='Nome completo',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Digite seu nome completo'
        })
    )
    email = forms.EmailField(
        required=True,
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Digite seu e-mail'
        })
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Digite sua senha'
        })
    )
    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirme sua senha'
        })
    )
    aceitar_termos = forms.BooleanField(
        required=True,
        label='Aceito receber novidades e promoções',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError(
                'E-mail inválido. Verifique o endereço e tente novamente.'
            )
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.is_active = True
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    """Formulário de login"""
    username = forms.CharField(
        max_length=150,
        label='E-mail',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Insira seu e-mail'
        })
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Insira sua senha'
        })
    )


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={
                'class': 'form-textarea feedback-textarea',
                'rows': 5,
                'placeholder': 'Conte-nos sua sugestão, elogio ou problema...',
                'required': True,
            })
        }


class AvaliacaoForm(forms.ModelForm):
    """Formulário de avaliação"""
    class Meta:
        model = Avaliacao
        fields = ['estrelas', 'comentario']
        widgets = {
            'estrelas': forms.RadioSelect(attrs={'class': 'star-rating'}),
            'comentario': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 4,
                'placeholder': 'Deixe seu comentário sobre este estabelecimento...'
            })
        }
