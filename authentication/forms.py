from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authentication.models import CustomUser


class SiginUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Escolha seu Usuario",
                "class":"form-control",
            }
        )
    )
    nome = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Seu nome",
                "class":"form-control",
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Digite seu Email",
                "class":"form-control",
                
            }
        )
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Digite uma senha",
                "class":"form-control",
                
            }
        )
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Confirme sua Senha",
                "class":"form-control",
            }
        )
    )
    class Meta:
        model = CustomUser
        fields = ('username','nome','email','password1','password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"usuario",
                "class":"form-control",
            }
        )
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Senha",
                "class":"form-control",
            }
        )
    )
    class Meta:
        fields = ('username','password')