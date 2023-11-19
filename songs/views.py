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


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'songs/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect('songs:detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'songs/detail.html', {'post': post, 'comments': comments, 'form': form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('songs:index')
    else:
        form = PostForm()
    return render(request, 'songs/create.html', {'form': form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('songs:index')
    else:
        form = PostForm(instance=post)
    return render(request, 'songs/update.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect('songs:index')
    return render(request, 'songs/delete.html', {'post': post})

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(
                reverse('songs:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'songs/comment.html', context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'songs/categories.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'songs/category.html', {'category': category})