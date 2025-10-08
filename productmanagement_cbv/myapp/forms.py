from django import forms
from myapp.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =['name','price']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <=0:
            return forms.ValidationError("Price must be greater than 0")
        return price