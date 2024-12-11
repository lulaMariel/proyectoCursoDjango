from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length = 100, label = 'Nombre', required = True)
    email = forms.EmailField(label = 'Email', required = True)
    contenido = forms.CharField(label = 'Contenido', widget=forms.Textarea)