from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
import os


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_category', args=[str(self.slug)])


class Post(models.Model):
    def thumbnail_path(instance, filename):
        basefilename, file_extension = os.path.splitext(filename)
        return 'img/blog/thumbnail/{title}{ext}'.format(title=instance.slug, ext=file_extension)

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    content = RichTextUploadingField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail_img = models.ImageField(upload_to=thumbnail_path)
    is_draft = models.BooleanField(
        verbose_name='Sauvegarder comme brouillon', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_post', args=[str(self.slug)])
