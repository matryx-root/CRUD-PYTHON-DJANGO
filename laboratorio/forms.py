from django import forms
from .models import Laboratorio


class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el país'}),
        }
