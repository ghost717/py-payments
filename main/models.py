from django.db import models

# Create your models here.
# class Category(models.Model):
#     RODZAJE = {
#         (0, 'Płatność'),
#         (1, 'Płatność stała'),
#         (2, 'Wpływ'),
#     }
#     cat = models.IntegerField(default=0,choices=RODZAJE)

class Cat(models.Model):
    RODZAJE = {
        (0, 'Płatność'),
        (1, 'Płatność stała'),
        (2, 'Wpływ'),
    }
    cat = models.IntegerField(default=0,choices=RODZAJE)

class Payment(models.Model):
    category = models.ForeignKey(Cat, on_delete=models.CASCADE) # rel on to many
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name # return self.name