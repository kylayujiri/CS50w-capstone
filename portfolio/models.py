from django.contrib.auth.models import AbstractUser
from django.db import models

def file_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Artist(AbstractUser):
    short_bio = models.CharField(max_length=60, blank=True)
    long_bio = models.CharField(max_length = 540, blank=True)
    location = models.CharField(max_length = 30, blank=True)
    show_email = models.BooleanField(null=False, default=False)
    website = models.URLField(blank=True)
    twitter = models.SlugField(max_length=15, blank=True)
    instagram = models.CharField(max_length=30, blank=True)


class Work(models.Model):
    image = models.ImageField(upload_to=file_path)
    title = models.CharField(max_length=60, blank=False)
    description = models.CharField(max_length=540, blank=True, null=True)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, null=False, related_name='work')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name="works")
    artists_liked = models.ManyToManyField('Artist', blank=True, related_name="liked_works")
    albums = models.ManyToManyField('Album', blank=True, related_name="works")

    def __str__(self):
        return f"{self.title} by {self.artist.username}"


class Comment(models.Model):
    commenter = models.ForeignKey('Artist', on_delete=models.CASCADE, null=False, related_name='comment')
    content = models.CharField(max_length=280, blank=False)
    work = models.ForeignKey('Work', on_delete=models.CASCADE, null=False, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    time_posted = models.DateTimeField(auto_now_add=True)
    artists_liked = models.ManyToManyField('Artist', blank=True, related_name="liked_comments")

    def __str__(self):
        return f"{self.commenter.username} on {self.work.title}"


class Album(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=540, blank=True)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, blank=False, null=False, related_name="albums")
    front_work = models.ForeignKey('Work', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.artist.username}"


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=280)

    def __str__(self):
        return f"{self.name}"
