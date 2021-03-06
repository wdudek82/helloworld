from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Playing with abstract models
class Parent(models.Model):
    name = models.ForeignKey('auth.User')
    flag = models.BooleanField()

    class Meta:
        abstract = True


class Hello(Parent, models.Model):
    title = models.CharField(max_length=100, default='- empty title -')
    message = models.TextField()

    def __str__(self):
        return self.name.username


class Example(Parent, models.Model):
    tag = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name.username

    def get_abs(self):
        return reverse('app1:example', kwargs={'slug': self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Example.ebjects.filter(slug=slug).order_by('-id')
    if qs.exists():
        new_slug = '{}-{}'.format(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_example_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_example_receiver, sender=Example)
