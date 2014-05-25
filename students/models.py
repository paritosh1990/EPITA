from django.db import models
from django.template.defaultfilters import slugify


class Student(models.Model):
    user_name = models.CharField(max_length=2500, blank=True, default='')
    slug = models.SlugField(max_length=255, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=2500, blank=True, default='')
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user_name)
        super(Student, self).save(*args, **kwargs)