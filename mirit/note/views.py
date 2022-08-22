from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

from .forms import NoteForm
from .models import Note, User


class PostListView(ListView):
    model = Note
    template_name = 'note/index.html'
    paginate_by = 20


class PostDetailView(DetailView):
    model = Note
    template_name = 'note/post_detail.html'


class ProfileDetailView(ListView):
    model = Note
    template_name = 'note/profile.html'
    paginate_by = 20

    def get_queryset(self):
        username = self.kwargs.get('pk')
        author = get_object_or_404(User, pk=username)
        q = author.pub_author.all()
        return q


class PostCreateView(CreateView):
    template_name = 'note/create_post.html'
    form_class = NoteForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class PostUpdateView(UpdateView):
    model = Note
    template_name = 'note/create_post.html'
    form_class = NoteForm
