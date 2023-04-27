from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateUserForm(UserCreationForm):
    username = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'class':'form-control m-1 p-1','placeholder':'Nombre de Usuario'}))
    email = forms.EmailField(help_text=None, label=False, widget=forms.EmailInput(attrs={'class':'form-control m-1 p-1','placeholder':'Email'}))
    password1 = forms.CharField(help_text=None, label=False, widget=forms.PasswordInput(attrs={'class':'form-control m-1 p-1','placeholder':'Contraseña'}))
    password2 = forms.CharField(help_text=None, label=False, widget=forms.PasswordInput(attrs={'class':'form-control m-1 p-1','placeholder':'Confirmar Contraseña'}))
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class LoginForm(AuthenticationForm):

    username = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'class':'form-control m-1 p-1','placeholder':'Nombre de Usuario'}))
    password = forms.CharField(help_text=None, label=False, widget=forms.PasswordInput(attrs={'class':'form-control m-1 p-1','placeholder':'Contraseña'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

class UpdateUserForm(forms.ModelForm):

    email = forms.EmailField(help_text=None, label=False, widget=forms.EmailInput(attrs={'class':'form-control m-1 p-1','placeholder':'Email'}))
    first_name = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'class':'form-control m-1 p-1','placeholder':'Nombre'}))
    full_name = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'class':'form-control m-1 p-1','placeholder':'Nombre Completo'}))
    last_name = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'class':'form-control m-1 p-1','placeholder':'Apellido'}))
    username = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'class':'form-control m-1 p-1','placeholder':'Nombre de Usuario'}))

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'full_name',
            'last_name',
            'username',
        ]
        