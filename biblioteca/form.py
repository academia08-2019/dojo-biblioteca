from biblioteca.models import Livro
from django import forms

class LivroForm(forms.ModelForm):
    model = Livro
    
