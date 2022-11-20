from django.contrib import admin

from .models import Note, User, ManyToManyTest, ManyPole


class NoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'title', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Note, NoteAdmin)
admin.site.register(User)
admin.site.register(ManyToManyTest)
admin.site.register(ManyPole)

