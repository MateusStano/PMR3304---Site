from django.forms import ModelForm
from .models import Album, Review


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            'name',
            'release_year',
            'poster_url',
            'info',
        ]
        labels = {
            'name': 'Título',
            'release_year': 'Ano de Lançamento',
            'poster_url': 'URL do poster',
            'info': 'Informações do Álbum'
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'text',
        ]
        labels = {
            'text': 'Resenha',
        }
