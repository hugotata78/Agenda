from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    CHOICE = (
        ('pendiente', 'PENDIENTE'),
        ('hecho', 'HECHO'),
    )
    title = forms.CharField(help_text=None, label=False, widget=forms.TextInput(attrs={'class':'form-control m-1 p-1','placeholder':'Ingrese un tilulo'}))
    description = forms.CharField(help_text=None, label=False, widget=forms.Textarea(attrs={'class':'form-control m-1 p-1','placeholder':'Ingrese la descripcion'}))
    done = forms.ChoiceField(label=False,choices=CHOICE, widget=forms.Select(attrs={'class':'form-control m-1 p-1'}))
    class Meta:
        model = Todo
        fields = [
            'title',
            'description',
            'done',
        ]