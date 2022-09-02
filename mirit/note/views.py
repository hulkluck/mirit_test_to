from xml.dom import ValidationErr
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from datetime import date, datetime

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


class PostStatView(ListView):
    model = Note
    paginate_by = 10
    template_name = 'note/stat.html'

    def get_queryset(self):
        def_val = datetime.now()
        start_date = self.request.GET.get('start', def_val)
        end_date = self.request.GET.get('end', def_val)
        new_context = Note.objects.filter(pub_date__gte=start_date, pub_date__lte=end_date)
        return new_context

    def get_context_data(self, **kwargs):
        def_val = datetime.now()
        context = super(PostStatView, self).get_context_data(**kwargs)
        context['start'] = self.request.GET.get('start', def_val)
        context['end'] = self.request.GET.get('end', def_val)
        context['count'] = Note.objects.all()
        return context
