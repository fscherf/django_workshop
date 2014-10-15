from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)

    author = models.ForeignKey(
        User,
        related_name='+',
        verbose_name='Author',
        blank=True,
        null=True
    )

    published = models.BooleanField(
        verbose_name='Published',
        default=False
    )

    title = models.CharField(
        verbose_name='Title',
        blank=False,
        max_length=35
    )

    content = models.TextField(
        verbose_name='Content',
    )

    created = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True
    )
