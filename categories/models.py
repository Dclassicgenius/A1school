from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    cat=(('HTML','HTML'),('CSS','CSS'),('JS','JS'))
    category_name = models.CharField(max_length=50, unique=True, choices=cat)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('quiz_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

class Subcategory(models.Model):
    cat=(('beginner','beginner'),('intermediate','intermediate'),('advanced','advanced'))
    sub_category_name = models.CharField(max_length=50, unique=True, choices=cat)
    sub_slug = models.SlugField(max_length=100, unique=True)
    sub_description = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'sub-category'
        verbose_name_plural = 'sub-categories'

    def get_url(self):
            return reverse('quiz_by_sub-category', args=[self.sub_slug])

    def __str__(self):
        return self.sub_category_name
