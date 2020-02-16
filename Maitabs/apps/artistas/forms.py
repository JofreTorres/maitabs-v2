from django.forms import ModelForm
from .models import Artista

class ArtistaForm(ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'
