from django.forms import ModelForm
from .models import Musica

class MusicaForm(ModelForm):
    class Meta:
        model = Musica
        exclude = ['slug']
