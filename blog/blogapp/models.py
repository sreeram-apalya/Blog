from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
# from django.core.urlresolvers import reverse
from django.urls import reverse
from taggit.managers import TaggableManager


class CustomManager(models.Manager):
    def abc(self):
        return super().abc().filter(status='published')


class Blog(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=300)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE,)
    Description=models.TextField()
    Image=models.ImageField(null=True,blank=True,upload_to='static/images')
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=CustomManager()
    tags=TaggableManager()

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    def get_list(self):
        return reverse('post_detail', self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    Description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return 'commented by {} on {}'.format(self.name,self.post)



