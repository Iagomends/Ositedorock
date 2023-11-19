from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import movie_data
from django.http import HttpResponseRedirect
from .models import Song
from .models import Post, Comment, Category

from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404


from .forms import PostForm, CommentForm

from django.views import generic


class SongListView(generic.ListView):
    model = Post
    template_name = 'songs/index.html' 

class SongDetailView(generic.DetailView):
    model = Post
    template_name = 'songs/detail.html'

class SongCreateView(generic.CreateView):
    model = Post
    fields = ['name', 'lyrics', 'band',]
    template_name = 'songs/create.html'
    success_url = '../'

class SongUpdateView(generic.UpdateView):
    model = Post
    fields = ['name', 'lyrics', 'band',]
    template_name = 'songs/update.html'
    success_url = '../../'

class SongDeleteView(generic.DeleteView):
    model = Post
    template_name = 'songs/delete.html'
    success_url = '../../'

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            posts=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('songs:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'songs/comment.html', context)

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'songs/categories.html'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'songs/category.html'