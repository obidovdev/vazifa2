from django.shortcuts import render ,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post



@login_required
def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)

def post_created(request):
    return render(request, 'blog/post_created.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            form.instance.author = user
            form.save()
            return redirect('blog:created_post')
    else:
        form = PostForm()
    return render(request, 'blog/post_created.html', {'form': form})