from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
   # return render(request, 'blog/blog_detail.html', {'post': post})
