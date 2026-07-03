from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Post


@login_required(login_url='accounts:login')
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.likes_count = 0
            post.comments_count = 0
            post.save()

            request.user.posts_count += 1
            request.user.save()

            return redirect('accounts:profile')
    else:
        form = PostForm()

    return render(request, 'posts/post_create.html', {'form': form})


@login_required(login_url='accounts:login')
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_liked = post.liked_users.filter(pk=request.user.pk).exists()
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            post.comments_count += 1
            post.save()

            return redirect('posts:detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'is_liked': is_liked,
        'comments': comments,
        'comment_form': comment_form,
    })


@login_required(login_url='accounts:login')
def post_like_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.liked_users.filter(pk=request.user.pk).exists():
        post.liked_users.remove(request.user)
        if post.likes_count > 0:
            post.likes_count -= 1
        post.save()
    else:
        post.liked_users.add(request.user)
        post.likes_count += 1
        post.save()

    return redirect(request.META.get('HTTP_REFERER', 'accounts:index'))
