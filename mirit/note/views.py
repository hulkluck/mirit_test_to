from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from mirit.settings import POSTS_PER_PAGE

from .forms import NoteForm
from .models import Note, User


def paginator_inside(request, post_list):
    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def index(request):
    post_list = Note.objects.all()
    page_obj = paginator_inside(request, post_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'note/index.html', context)

def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = author.pub_author.all()
    page_obj = paginator_inside(request, post_list)
    sum_count = post_list.count()
    context = {
        'author': author,
        'sum_count': sum_count,
        'page_obj': page_obj,
    }
    return render(request, 'note/profile.html', context)

def note_detail(request, note_id):
    post = get_object_or_404(Note, pk=note_id)
    sum_count = Note.objects.filter(author=post.author).count()
    context = {
        'post': post,
        'sum_count': sum_count,
    }
    return render(request, 'note/post_detail.html', context)

@login_required
def note_create(request):
    form = NoteForm(
        request.POST or None
    )
    if form.is_valid():
        post = form.save(False)
        post.author = request.user
        post.save()
        username = post.author.username
        return redirect('notes:profile', username)
    return render(request,
                  'note/create_post.html', {'form': form})


@login_required
def note_edit(request, note_id):
    post = get_object_or_404(Note, pk=note_id)
    form = NoteForm(
        request.POST or None,
        instance=post
    )
    if form.is_valid():
        form.save()
        return redirect('notes:note_detail', post.pk)
    return render(request, 'note/create_post.html',
                  {'form': form, 'is_edit': True, 'post_id': note_id})