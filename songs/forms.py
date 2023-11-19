from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'band',
            'lyrics',
        ]
        labels = {
            'name': 'Título',
            'band': 'Banda',
            'lyrics': 'Letra',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }