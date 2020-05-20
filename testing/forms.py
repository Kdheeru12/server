from django import forms

class Ordersforms(forms.Form):
    name = forms.CharField(max_length=40)
    phonenumber = forms.CharField(max_length=10)
    alt_number = forms.CharField(max_length=10)
    address = forms.CharField(max_length=800)
    landmark = forms.CharField(max_length=300)
    ordered = forms.FileField()
        