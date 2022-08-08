from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('create/', views.note_create, name='note_create'),
    path('note/<note_id>/edit/', views.note_edit, name='note_edit'),
]
