# Generated by Django 3.1 on 2021-06-11 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('link', models.URLField(verbose_name='link')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('vote_count', models.IntegerField(verbose_name='number_of_votes')),
                ('author', models.CharField(max_length=25, verbose_name='author')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=25, verbose_name='author')),
                ('text', models.CharField(max_length=225, verbose_name='text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.post', verbose_name='post')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
