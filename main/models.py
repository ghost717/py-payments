from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Post(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default="Title")
    content = models.TextField(default="")
    date = models.DateField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='post') #(null=True, blank=True, upload_to='plakaty')
    
    def __str__(self):
        return self.title

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)

class Images(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')

# class Images(models.Model):
#     post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='gallery',verbose_name='Image')

class Cat(models.Model):
    RODZAJE = {
        (0, 'Płatność'),
        (1, 'Płatność stała'),
        (2, 'Wpływ'),
    }
    cat = models.IntegerField(default=0,choices=RODZAJE)

    # def __str__(self):
    #     return self.RODZAJE

class Payment(models.Model):
    category = models.ForeignKey(Cat, on_delete=models.CASCADE) # rel on to many
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    valueType = models.IntegerField(null=True, blank=True, default=-1)

    def __str__(self):
        return self.name # return self.name

class Treningi(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    ex01 = models.CharField(max_length=30, null=True, blank=True)
    ex02 = models.CharField(max_length=30, null=True, blank=True)
    ex03 = models.CharField(max_length=30, null=True, blank=True)
    ex04 = models.CharField(max_length=30, null=True, blank=True)
    ex05 = models.CharField(max_length=30, null=True, blank=True)
    ex06 = models.CharField(max_length=30, null=True, blank=True)
    ex07 = models.CharField(max_length=30, null=True, blank=True)
    ex08 = models.CharField(max_length=30, null=True, blank=True)
    ex09 = models.CharField(max_length=30, null=True, blank=True)
    ex10 = models.CharField(max_length=30, null=True, blank=True)