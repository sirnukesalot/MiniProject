from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import PostForm, CommentForm
from blog.models import Post
from blog.models import Comment


# Create your views here.
def all_posts(request):
    posts = Post.objects.all()
    posts_form = PostForm(request.POST)
    if request.method == "POST":
        if posts_form.is_valid():
            post = posts_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('all_posts', pk=post.pk)
    return render(request, 'blog/post_list.html', {'posts': posts, 'posts_form': posts_form})


def single_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


@login_required()
def post_create(request):
    posts = Post.objects.all()
    posts_form = PostForm(request.POST)
    if request.method == "POST":
        if posts_form.is_valid():
            post = posts_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_form.html', {'posts': posts, 'posts_form': posts_form})


@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
    return redirect('all_posts')
