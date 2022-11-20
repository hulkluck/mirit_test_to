# Generated by Django 4.0.6 on 2022-11-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0008_manytomanytest_manypole'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manypole',
            name='many',
        ),
        migrations.AddField(
            model_name='manytomanytest',
            name='pole_photo',
            field=models.ManyToManyField(related_name='photo_1', to='note.manypole'),
        ),
    ]
