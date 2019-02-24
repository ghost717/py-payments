from django.db import models

# Create your models here.
# class Category(models.Model):
#     RODZAJE = {
#         (0, 'Płatność'),
#         (1, 'Płatność stała'),
#         (2, 'Wpływ'),
#     }
#     cat = models.IntegerField(default=0,choices=RODZAJE)

class Post(models.Model):
    title = models.CharField(max_length=120, default="Title")
    content = models.TextField(default="")
    date = models.DateField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='post') #(null=True, blank=True, upload_to='plakaty')
    
    def __str__(self):
        return self.title

class Images(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery',verbose_name='Image')

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

    def __str__(self):
        return self.name # return self.name