# Generated by Django 4.1 on 2022-11-19 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_manytomanytest_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manypole',
            name='photo',
            field=models.FileField(null=True, upload_to='many_test'),
        ),
        migrations.RemoveField(
            model_name='manytomanytest',
            name='photo',
        ),
        migrations.AddField(
            model_name='manytomanytest',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='many_pole', to='note.manypole'),
        ),
    ]
