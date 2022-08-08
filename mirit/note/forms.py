from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Note


class NoteForm(forms.ModelForm):

    class Meta:

        model = Note
        fields = ('title', 'text')
        labels = {
            'title': _('Заголовок заметки'),
            'text': _('Текст заметки'),
        }
        help_texts = {
            'title': _('Здесь текст заголовка для фашей заметки'),
            'text': _('Здесь текст вашей заметки'),
        }

        def clean_text(self):
            text = self.cleaned_data['text']

            if text == '':
                raise forms.ValidatorError(
                    'В заметке обязательно должен быть текст'
                )
            return text