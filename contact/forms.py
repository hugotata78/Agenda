from django import forms
from .models import Contact

class CreateContactForm(forms.ModelForm):

    name = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'class':'form-control m-1 p-1','placeholder':'Nombre'}))
    email = forms.EmailField(help_text=None, label=False, widget=forms.EmailInput(attrs={'class':'form-control m-1 p-1','placeholder':'Email'}))
    movil = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'class':'form-control m-1 p-1','placeholder':'Movil'}))
    phone = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'class':'form-control m-1 p-1','placeholder':'Teléfono'}))
                            

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'movil',
            'phone',
        ]

