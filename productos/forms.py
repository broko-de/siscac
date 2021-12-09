from django import forms
from django.forms import fields

from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model= Producto
        fields= '__all__'