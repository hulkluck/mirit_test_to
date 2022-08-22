from django.urls import path

from .views import *

app_name = 'notes'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('note/<int:pk>/', PostDetailView.as_view(), name='note_detail'),
    path('create/', PostCreateView.as_view(), name='note_create'),
    path('note/<int:pk>/edit/', PostUpdateView.as_view(), name='note_edit'),
]
