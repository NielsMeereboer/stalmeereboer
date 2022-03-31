from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(null=True, blank=True, upload_to="newsimages/")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.header_image.path)

        if img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.header_image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Hengst(models.Model):
    hengst_title = models.CharField(max_length=100)
    hengst_image = models.ImageField(null=True, blank=True, upload_to="hengstimages/")
    hengst_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hengst_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.hengst_image.path)

        if img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.hengst_image.path)

    def get_absolute_url(self):
        return reverse('hengst-detail', kwargs={'pk': self.pk})