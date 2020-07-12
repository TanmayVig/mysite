from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Comment, Post
from blog.forms import CommentForm, PostForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView,)

app_name = 'blog'
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class postListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class postDetailView(DetailView):
    model = Post

class cratePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class postUpdateView(LookupError, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    model = Post
    success_url = reverse_lazy('blog:post_list')

class DraftView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('creat_date')


###########################################
###########################################
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog:post_detail',pk = post.pk)

    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})


@login_required
def commentApprove(request,pk):
    comment = get_object_or_404(Comment, pk= pk)
    comment.appreve()
    return redirect('blog:post_detail', pk = comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = commnet.post.pk
    # we did not call directly the pk because the
    #

    # comment will get deleted and the pk will not be remembered
    comment.delete()

    return redirect('blog:post_detail',pk = post_pk)


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk = pk)
