from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('notes:note_detail', args=[self.id])

    def __str__(self):
        return self.text[:15]
        


class ManyPole(models.Model):
    photo = models.ImageField(upload_to='many_test', null=True)
    # many = models.ForeignKey('ManyToManyTest', on_delete=models.CASCADE, related_name='many_pole')


class ManyToManyTest(models.Model):
    YESNO = (
        ('ДА', 'ДА'),
        ('НЕТ', 'НЕТ')
    )
    user = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    pole = models.CharField(verbose_name='Вопрос', choices=YESNO, max_length=3)
    pole_photo = models.ManyToManyField(ManyPole, related_name='photo_1')

    def get_absolute_url(self):
        return reverse('notes:index')
