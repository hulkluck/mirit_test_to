from xml.dom import ValidationErr
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    FormView,
)
from datetime import date, datetime

from .forms import NoteForm, ManyForm, PhotoFileForm
from .models import Note, User, ManyPole, ManyToManyTest


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


class CreateMany(FormView):
    template_name = 'note/many.html'
    form_photo = PhotoFileForm
    form_quest = ManyForm

    def get_success_url(self):
        return reverse ('notes:many')

    def get(self, request, *args, **kwargs):
        context = {'form_quest': self.form_quest, 'form_photo': self.form_photo}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.object = None
        form_quest = ManyForm(request.POST or None, request.FILES or None)
        form_photo = PhotoFileForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('photo')
        if form_quest.is_valid() and form_photo.is_valid():
            f_q = form_quest.save(commit=False)
            f_q.user = self.request.user
            f_q.save()
            for f in files:
                f_p = ManyPole(photo=f)
                f_p.save()
                f_q.pole_photo.add(f_p.id)           
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form_quest)


class ManyView(ListView):
    model = ManyToManyTest
    template_name = 'note/many_list.html'
