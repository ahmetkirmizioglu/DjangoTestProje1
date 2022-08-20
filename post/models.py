from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Yazar', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120,verbose_name="İlan Başlığı")
    content = models.TextField(verbose_name="İlan Açıklama")
    publishing_date = models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True)
    image = models.FileField(null=True, blank=True, verbose_name='İlan Resmi')
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    map_location = models.TextField(null=True, blank=True, verbose_name="Harita Konumu<br><em class='em12'>Örnek : https://www.google.com/maps/embed?pb=xxxxxxxxx</em>")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'id': self.id})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter=1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
            return unique_slug


    def save(self, *args, **kwargs):
        #self.slug = self.get_unique_slug()
        self.slug = slugify(self.title.replace('ı', 'i'))
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date']
        # return "/post/{}".format(self.id)