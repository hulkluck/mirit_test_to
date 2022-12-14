# Generated by Django 4.0.6 on 2022-11-19 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_remove_manytomanytest_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManyToManyTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pole', models.CharField(choices=[('ДА', 'ДА'), ('НЕТ', 'НЕТ')], max_length=3, verbose_name='Вопрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ManyPole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='many_test')),
                ('many', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='many_pole', to='note.manytomanytest')),
            ],
        ),
    ]
