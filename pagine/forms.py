from django import forms

class ContattoForm(forms.Form):
    nome = forms.CharField(required=True, max_length=100, label='Nome')
    email = forms.EmailField(required=False, label='e-mail')
    argomento = forms.CharField(required=True, max_length=100)
    messaggio = forms.CharField(required=True, widget=forms.Textarea)