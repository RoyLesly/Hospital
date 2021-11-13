from django import forms
from .models import Patient, Purpose


class RegPatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'
        widgets={
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'from forms.py'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PurposeForm(forms.ModelForm):

    class Meta:
        model = Purpose
        fields = '__all__'
        widgets={
            'purpose': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'from forms.py'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
        }