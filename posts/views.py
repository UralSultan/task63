from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PostForm


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
