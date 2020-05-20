from django  import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('name','phonenumber','alt_number','address','landmark','ordered')