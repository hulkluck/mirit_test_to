from django.db import models
from django.contrib.auth.models import AbstractUser


ADMIN = 'admin'
MODERATOR = 'moderator'
USER = 'user'

CHOICES = (
    (ADMIN, ADMIN),
    (MODERATOR, MODERATOR),
    (USER, USER),
)


class User(AbstractUser):

    fio = models.TextField(
        verbose_name='ФИО'
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения',
        null=True,
        blank=True
    )
    srole = models.CharField(
        'Статус пользователя',
        max_length=20,
        choices=CHOICES,
        default=USER
    )

    @property
    def is_admin(self):
        return (
            self.role == ADMIN or self.is_staff
            or self.is_superuser
        )

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Note(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок заметки'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    text = models.TextField(
        verbose_name='Текст заметки'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pub_author',
        verbose_name='Автор заметки'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.text[:15]
