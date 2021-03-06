from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django import forms


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

        if img.width > 450:
            output_size = (450, 450)
            img.thumbnail(output_size)
            img.save(self.header_image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Hengst(models.Model):
    hengst_title = models.CharField(max_length=100)
    hengst_image = models.ImageField(null=True, blank=True, upload_to="hengstimages/")
    hengst_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    stokmaat = models.CharField(max_length=100, default='SOME STRING')
    kleur = models.CharField(max_length=100, default='SOME STRING')
    father_name = models.CharField(max_length=100, default='SOME STRING')
    mother_name = models.CharField(max_length=100, default='SOME STRING')
    fatherfather_name = models.CharField(max_length=100, default='SOME STRING')
    fathermother_name = models.CharField(max_length=100, default='SOME STRING')
    motherfather_name = models.CharField(max_length=100, default='SOME STRING')
    mothermother_name = models.CharField(max_length=100, default='SOME STRING')

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


class Sale(models.Model):
    title = models.CharField(max_length=250)
    stokmaat = models.CharField(max_length=100, default='SOME STRING')
    kleur = models.CharField(max_length=100, default='SOME STRING')
    prijs = models.CharField(max_length=100, default='SOME STRING')
    description = models.TextField()
    image = models.ImageField(blank=True)
    father_name = models.CharField(max_length=100, default='SOME STRING')
    mother_name = models.CharField(max_length=100, default='SOME STRING')
    fatherfather_name = models.CharField(max_length=100, default='SOME STRING')
    fathermother_name = models.CharField(max_length=100, default='SOME STRING')
    motherfather_name = models.CharField(max_length=100, default='SOME STRING')
    mothermother_name = models.CharField(max_length=100, default='SOME STRING')

    def __str__(self):
        return self.title


class PostImage(models.Model):
    sale = models.ForeignKey(Sale, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.sale.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.images.path)

        if img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.images.path)


class About(models.Model):
    title = models.CharField(max_length=100)
    about_image = models.ImageField(null=True, blank=True, upload_to="aboutimages/")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.about_image.path)

        if img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.about_image.path)

    def get_absolute_url(self):
        return reverse('about-detail', kwargs={'pk': self.pk})


class Merrie(models.Model):
    merrie_title = models.CharField(max_length=100)
    merrie_image = models.ImageField(null=True, blank=True, upload_to="merrieimages/")
    merrie_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    stokmaat = models.CharField(max_length=100, default='SOME STRING')
    kleur = models.CharField(max_length=100, default='SOME STRING')
    father_name = models.CharField(max_length=100, default='SOME STRING')
    mother_name = models.CharField(max_length=100, default='SOME STRING')
    fatherfather_name = models.CharField(max_length=100, default='SOME STRING')
    fathermother_name = models.CharField(max_length=100, default='SOME STRING')
    motherfather_name = models.CharField(max_length=100, default='SOME STRING')
    mothermother_name = models.CharField(max_length=100, default='SOME STRING')

    def __str__(self):
        return self.merrie_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.merrie_image.path)

        if img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.merrie_image.path)

    def get_absolute_url(self):
        return reverse('merrie-detail', kwargs={'pk': self.pk})


class Veulen(models.Model):
    veulen_title = models.CharField(max_length=100)
    veulen_image = models.ImageField(null=True, blank=True, upload_to="veulenimages/")
    veulen_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    kleur = models.CharField(max_length=100, default='SOME STRING')
    father_name = models.CharField(max_length=100, default='SOME STRING')
    mother_name = models.CharField(max_length=100, default='SOME STRING')
    fatherfather_name = models.CharField(max_length=100, default='SOME STRING')
    fathermother_name = models.CharField(max_length=100, default='SOME STRING')
    motherfather_name = models.CharField(max_length=100, default='SOME STRING')
    mothermother_name = models.CharField(max_length=100, default='SOME STRING')

    def __str__(self):
        return self.veulen_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.veulen_image.path)

        if img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.veulen_image.path)

    def get_absolute_url(self):
        return reverse('veulen-detail', kwargs={'pk': self.pk})


class Paard(models.Model):
    paard_title = models.CharField(max_length=100)
    paard_image = models.ImageField(null=True, blank=True, upload_to="paardimages/")
    paard_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    geslacht = models.CharField(max_length=100, default='SOME STRING')
    geboortedatum = models.CharField(max_length=100, default='DD-MM-YYYY')
    kleur = models.CharField(max_length=100, default='SOME STRING')
    stokmaat = models.CharField(max_length=100, default='SOME STRING')
    father_name = models.CharField(max_length=100, default='SOME STRING')
    mother_name = models.CharField(max_length=100, default='SOME STRING')
    fatherfather_name = models.CharField(max_length=100, default='SOME STRING')
    fathermother_name = models.CharField(max_length=100, default='SOME STRING')
    motherfather_name = models.CharField(max_length=100, default='SOME STRING')
    mothermother_name = models.CharField(max_length=100, default='SOME STRING')

    def __str__(self):
        return self.paard_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.paard_image.path)

        if img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.paard_image.path)

    def get_absolute_url(self):
        return reverse('paard-detail', kwargs={'pk': self.pk})


class Nieuws(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class NieuwsImage(models.Model):
    nieuws = models.ForeignKey(Nieuws, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='newsimages/')

    def __str__(self):
        return self.nieuws.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.images.path)

        if img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.images.path)