from django import forms


class KPIForm(forms.Form):
    csv = forms.FileField()
