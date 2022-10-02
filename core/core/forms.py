from django import forms
from .models import Venta, Catalogo


class FormVenta(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = (
            'nombre_producto',
            'nombre_vendedor',
            'marca_cicla',
            'precio',
            'ciudad',
            'contacto',
            'imagen',
        )
    
    def clean_price(self,  *args, **kwargs):
        price = self.cleaned_data.get('price')
        price = float(price)
        print(price)
        if price > 0:
            return price
        else:
            raise forms.ValidationError('Por favor, inserta un precio válido.')
