from django.db import models
from datetime import datetime
from tinymce import HTMLField

class Category(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    overview = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.now())
    slug = models.SlugField(max_length=250)
    body = HTMLField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %y')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'id': self.id
        })
