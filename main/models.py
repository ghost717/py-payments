from django.db import models

# Create your models here.
class Category(models.Model):
    RODZAJE = {
        (0, 'Płatność'),
        (1, 'Płatność stała'),
        (2, 'Wpływ'),
    }
    cat = models.IntegerField(default=0,choices=RODZAJE)

class Payment(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default="")
    value = models.IntegerField(null=True, blank=True)

    #rel 1-1
    info = models.OneToOneField(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name # return self.name