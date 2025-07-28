from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from .forms import BlogForm 


# Create your views here.
@login_required
def blog_list(request):
    posts = BlogPost.objects.filter(is_deleted=False).order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

@login_required
def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES) 
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            form.save_m2m() 
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogForm()
    return render(request, 'blog/blog_create.html', {'form': form})

@login_required
def blog_edit(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug, is_deleted=False, author=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_edit.html', {'form': form})

@login_required
def blog_delete(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug, author=request.user)
    blog.is_deleted = True
    blog.save()
    return redirect('blog_list')


@login_required
def my_blogs(request):
    blogs = BlogPost.objects.filter(author=request.user, is_deleted=False).order_by('-created_at')
    return render(request, 'blog/my_blogs.html', {'blogs': blogs})