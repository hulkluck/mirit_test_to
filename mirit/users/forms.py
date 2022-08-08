from django.contrib.auth.forms import UserCreationForm
from note.models import User


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('fio', 'username', 'birth_date',)
