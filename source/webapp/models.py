from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    author = models.CharField(_('author'), max_length=25)
    post = models.ForeignKey('Post', models.CASCADE, verbose_name=_('post'))
    text = models.CharField(_('text'), max_length=225)
    created = models.DateTimeField(_('created'), auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Post(models.Model):
    title = models.CharField(_('title'), max_length=150)
    link = models.URLField(_('link'))
    created = models.DateTimeField(_('created'), auto_now_add=True,)
    vote_count = models.IntegerField(_("number_of_votes"))
    author = models.CharField(_('author'), max_length=25)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
